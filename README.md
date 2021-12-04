# Georgia-Accountability-Court-Success-Pred# Georgia Accountability Court Success Prediction

Matthew Bishop, Ashley Gates, Raheem Paxton, Swapna Subbagari

## Introduction

Georgia’s accountability court programs offer an alternative to traditional adjudication and incarceration for non-violent offenders charged with various drug-related crimes and DUIs. The state of Georgia contracted with the Carl Vinson Institute of Government at the University of Georgia to estimate the financial benefits of accountability courts, finding that, on average, the programs saved the state of Georgia more than $22,000 per graduate. This study also found that accountability courts are almost $5,000 less than the costs for traditional adjudication per defendant when considering both state and local costs (https://cjcc.georgia.gov/document/full-report/download).
Considering these potential savings for the state, it’s no wonder that these programs are growing in popularity. This study aimed to identify the feature relevant for graduation and develop a prediction model that can be deployed for public use. 

![image](https://user-images.githubusercontent.com/82011523/144700881-a42dcc72-82f2-4f1c-a636-b609ea6ae1b4.png)


## Problem Statement--Questions to Examine

•	What features are most relevant for graduation?
•	Does time between arrest and acceptance impact graduation?
•	Are there certain individual characteristics that increase one’s risk for termination?

### Data points to examine:

•	Acceptance type

•	Age

•	Arrest date, 

•	Referral date

•	Risk level

•	Acceptance Date- Arrest Date → Processing Time(Mathew will get back to us)

•	Exit date

•	Exit status

•	Referral source

•	Demographic info: DOB, Education level(could change), Employment status(at entry), Gender, Income level, Employment stability, Military service, Race

•	Program type (See program codes below)

•	Clinical Diagnosis and Level

•	Diagnosis Reason

•	Number of drug tests

•	Count weekly judicial status meetings 

•	Primary drug of choice

•	Secondary drug of choice

•	Number of treatment sessions

•	Residence County



### Program Codes

•	FD - Felony Drug

•	DC - DUI Courts

•	MH - Mental Health

•	JD - Juvenile Drug

•	JM - Juvenile Mental Health

•	FT - Family Treatment

•	VC - Veterans Court

## Methodology and Results

### Data Cleaning

The data were cleaned by examining relevant data points and items that would move forward in the final analysis. Participants with unrealistic values were removed from the analytic data frame. 

### Descriptive Statistics

Descriptive statistics were computed for all variables of interest.  In particular, we examined the distribution of all continuous variables to determine whether they were normally distributed.  The frequency counts of all categorical variables were explored. Finally, we explored the pros and cons of scaling and binning continuous variables. 

### Unsupervised Learning

The data were pre-processed by one-hot-encoding (i.e., get_dummies) all categorical variables and standardizing continuous variables using StandardScaler in Pandas. We then fit a Principal Component Analysis specifying that the model accounts for 99% of the variance in the data. Finally, we used TSNE to reduce the identified components further and derived an Inertia plot to determine the relevant clusters in the data. 
The elbow plot did not suggest a definitive cluster number. However, after exploring two to four clusters on relevant features, we decided on two clusters because of their ability to distinguish participants on relevant factors. The clusters were later visualized with Matplotlib (See Below). 

![image](https://user-images.githubusercontent.com/82011523/144700898-5c0a1024-ff21-48ec-9e06-f68c56e76d40.png)


![image](https://user-images.githubusercontent.com/82011523/144700915-fd42fd85-c6d3-4317-88de-22226e148c66.png)


### Supervised Learning

Initially, we used Recursive Feature Elimination (RFE) with a Random Forest estimator to determine the number of features relevant for further testing.  The features were selected using using 5-fold cross-validation with 2 repeats, which produced mean accuracy and standard deviation scores for the 5 to 20 features that were evaluated (See figure below).  

![image](https://user-images.githubusercontent.com/82011523/144700928-a54705da-1b3e-435f-b066-026149308d52.png)


The model revealed that eight features produced a reasonable accuracy, which preserving model parsimony. We then trained a series of 5 machine learning models using a Recursive feature elimination pipeline, with 5-fold cross-validation, with two repeats.  The final model was chosen based on mean accuracy. 


![image](https://user-images.githubusercontent.com/82011523/144700954-c75892f8-0166-47e4-9ab7-0d2c9232af7c.png)

We observed that Gradient Boosting produced the highest accuracy.  The model was then tuned using a randomized grid search to obtain the best precision, specificity, recall, and R-square.  The unbalanced classification report was reported below. 


## Front End

The model is housed, along with other visualizations, in a Heroku (or similar tool) website. Other tools to be used to complete this project were Python Pandas, Tableau, Flask. HTML/CSS/Bootstrap, and SQL database. 

## Heroku App

The deployed app can be viewed [here]( https://ga-court-success-prediction.herokuapp.com/).

## Final Presentation

The final presentation can be viewed [here](https://docs.google.com/presentation/d/1AE77PszJ4ofK1i53RgwURCI_WWxfZl6L0TatMaF7tqk/edit#slide=id.gfc94c3dec1_0_75).
