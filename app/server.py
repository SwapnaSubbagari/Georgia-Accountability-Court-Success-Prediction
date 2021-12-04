#import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import sklearn

app = Flask(__name__)

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("finalized_model2.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
 
@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if result== 'Terminated/Discharged':
            prediction ='TERMINATED OR DISCHARGED'
        else:
            prediction ='GRADUATED OR COMPLETED'
            
                                
        return render_template("predict.html", 
        prediction = prediction,
        info = to_predict_list)

if __name__ == '__main__':
    app.run(port=5000, debug=True)