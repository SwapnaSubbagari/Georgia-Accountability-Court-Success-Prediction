# Georgia-Accountability-Court-Success-Pred# Georgia Accountability Court Success Prediction

Matthew Bishop, Ashley Gates, Raheem Paxton, Swapna Subbagari


## Introduction

Georgia’s accountability court programs offer an alternative to traditional adjudication and incarceration for non-violent offenders charged with a variety of drug related crimes and DUIs. The state of Georgia contracted with the Carl Vinson Institute of Government at the University of Georgia to estimate the fiscal benefits of accountability courts, finding that, on average, the programs  saved the state of Georgia more than $22,000 per graduate. This study also found that accountability courts are almost $5,000 less than the costs for traditional adjudication per defendant when considering both state and local costs (https://cjcc.georgia.gov/document/full-report/download).

Considering this potential sizable savings for the state, it’s no wonder that these types of programs are growing in popularity. This study will aim to predict characteristics in defendants that make them good potential graduates of an accountability program. 


## Problem Statement--Questions to Examine

Application will be used by the court system to predict whether arrestees are good candidates for drug court. How determinate is the risk profile of the candidate as to whether or not a candidate will graduate from drug court? How determinate is the time frame between referral and acceptance to drug court in a candidate’s graduation status? 

## Methodology

Descriptive statistics will be computed for all variables of interest.  We will examine the distribution of all continuous variables to determine whether they were normally distributed and examine frequency counts of all categorical variables. Depending on the distribution of the data, techniques such as binning or combining categories will be discussed. 
 
The data will be cleaned by examining relevant data points as well as items that will move forward in the final analysis. Variables with greater than 25% of missing data will be removed from the analysis, whereas mean, median, and mode imputation will be used for those variables with less than 25% missing data will. Will will examine models with and without imputation to determine whether imputation had an impact on our final estimates.

Data will be pre-processed by created dummy variables for categorical variables (.get_dummies) and continuous variables will be normalized with StandardScaler.

We will examine several machine learning techniques to determine what method and model provides the best fit.  Initially, we will use random forest for feature selection procedures. Our random forest models will be computed in an iterative process.  We will examine the accuracy of difference models with differing numbers of features.  We will determine a relevant stopping based on change in multiple indices (i.e. accuracy, F1, etc).  In particular, a significant drop in accuracy and other scores will denote a stopping point. 

## Data points to examine:

Acceptance type
Age
Arrest date, 
Referral date
Risk level
Acceptance Date- Arrest Date → Processing Time(Mathew will get back to us)
Exit date
Exit status
Referral source
Demographic info: DOB, Education level(could change), Employment status(at entry), Gender, Income level, Employment stability, Military service, Race
Program type (is encoded in the ID)
Clinical Diagnosis and Level
Diagnosis Reason
Number of drug tests
Count weekly judicial status meetings 
Primary drug of choice
Secondary drug of choice
Number of treatment sessions
Phase 1 Date
Phase 2 date
Residence County



## Program Codes
FD - Felony Drug
DC - DUI Courts
MH - Mental Health
JD - Juvenile Drug
JM - Juvenile Mental Health
FT - Family Treatment
VC - Veterans Court


## Front End

Model will be housed, along with the potential for other visualizations, in a Heroku (or similar tool) website. Other tools to be used could include Python Pandas, Tableau, Flask. HTML/CSS/Bootstrap, and SQL database. 

## Heroku App

The deployed app can be viewed [here]( https://ga-court-success-prediction.herokuapp.com/)
