from logging import Logger
import logging
import sqlite3

from datetime import datetime, date
from flask import (Flask, json, render_template, jsonify, redirect, request, g)
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
import sqlite3
import pandas as pd
import csv
import pickle
import sklearn
import numpy as np



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def open_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    # load the data into a Pandas DataFrame
    users = pd.read_csv(r"newData.csv")
    # write the data to a sqlite table
    users.to_sql('data', conn, if_exists='replace', index = False)

open_db()

@app.route('/getGraduationStatusTypeCount')
def getGraduationStatusTypeCount():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('''SELECT STATUS, COUNT(*) AS count FROM data  GROUP BY status  ''').fetchall()
    
    conn.close()
    resp = []
    app.logger.info(data)
    for row in data:
        jsonData = {}
        jsonData["status"] = row["status"]
        jsonData["count"] = row["count"]
        resp.append(jsonData)
    return jsonify(resp)

@app.route('/getStatusBasedOnDrug')
def getStatusBasedOnDrug():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('''SELECT PRIMARY_DRUG_CHOICE, COUNT(*) AS count FROM data  GROUP BY PRIMARY_DRUG_CHOICE  ''').fetchall()
    resp = []
    app.logger.info(data)
    for row in data:
        jsonData = {}
        subDataList = []
        jsonData["drug"] = row["PRIMARY_DRUG_CHOICE"]
        drug = row["PRIMARY_DRUG_CHOICE"]
        qData = c.execute('''SELECT STATUS, COUNT(*) AS count FROM data WHERE PRIMARY_DRUG_CHOICE=? GROUP BY status ''',(drug,)).fetchall()
        for subRow in qData :
            subData = {}
            subData['status'] = subRow["status"]
            subData['count'] = subRow["count"]
            subDataList.append(subData)
        
        jsonData['statusList'] = subDataList
        resp.append(jsonData)
    
    conn.close()
    return jsonify(resp)


@app.route('/getStatusBasedOnEducation')
def getStatusBasedOnEducation():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('''SELECT EDUCATION_LEVEL, COUNT(*) AS count FROM data  GROUP BY EDUCATION_LEVEL  ''').fetchall()
    resp = []
    app.logger.info(data)
    for row in data:
        jsonData = {}
        subDataList = []
        jsonData["educaiton"] = row["EDUCATION_LEVEL"]
        educaiton = row["EDUCATION_LEVEL"]
        qData = c.execute('''SELECT STATUS, COUNT(*) AS count FROM data WHERE EDUCATION_LEVEL=? GROUP BY status ''',(educaiton,)).fetchall()
        for subRow in qData :
            subData = {}
            subData['status'] = subRow["status"]
            subData['count'] = subRow["count"]
            subDataList.append(subData)
        
        jsonData['statusList'] = subDataList
        resp.append(jsonData)
    
    conn.close()
    return jsonify(resp)

@app.route('/getAverageAgeByCount')
def getAverageAgeByCount():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    data = c.execute('''SELECT AGE FROM data ''').fetchall()
    conn.close()
    resp = []
    
    for row in data:
        jsonData = {}
        jsonData["dob"] = int(float(row["AGE"]))
        resp.append(jsonData["dob"])
    ages_data = pd.DataFrame({'age':resp})
    bins = [0,18,25,30,35,40,45,50,55,100]
    label = ['a1','a2','a3','a4','a5','a6','a7','a8','a9']
    ages_data['ageGroup']=pd.cut(ages_data['age'],bins=bins,labels=label,right=False,ordered=False)
    countAges = ages_data.groupby('ageGroup').count()
    countAgesList = countAges['age'].values.tolist();
    return jsonify(countAgesList);




@app.route("/sendData", methods=["POST"])
def post_javascript_data():
    return {
        "program_type": program_type,
        "diagnosis_reason": diagnosis_reason,
        "primary_drug_choice": primary_drug_choice,
        "education_level": education_level,
        "employement_status": employement_status,
        "age": age,
        "income_level": income_level,
        "acceptance_type": acceptance_type,
        "risk_level":risk_level,
    }


# ML MODEL API Call


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("finalized_model2.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())

        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if result== 'Terminated/Discharged':
            prediction =' ☹️ TERMINATED   OR   DISCHARGED'
        else:
            prediction =' 🎓 GRADUATED   OR   COMPLETED '
            
                                
        return render_template("ml.html", 
        prediction = prediction,
        info = to_predict_list)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/')
@app.route('/home')
def home():

    # Find one record of data from the mongo database
    # Result_Dict = results_collection.find_one()
    # Return template and data
    return render_template('home.html')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/about')
def about():
    return render_template('about.html')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.route('/ml',methods = ['POST','GET'])
def ml():
    return render_template('ml.html')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)
