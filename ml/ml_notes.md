<!-- Show-Markdown ml_notes.md -UseBrowser      for running it--> 
This conains topics I have learnt in it and some brief description about it

# Machine Learning
## Dates with their topics covered


###   28-01-2026 

Topics Covered:
- Supervised Learning
- UnSupervised Learning
- Semi-Supervised Learning


Why models fail reasons:
- Overfitting:Does not perform well on testing data
- Underfitting:Model is so simple. it did not learn anything
- Concept Drift:The inputs are totally different Ex:One is precovid data and other is post covid data
- Data Leakage:The testing data is leaked and this fails in production i.e in future it fails
- Insufficient Data:Data is not enough to predict the correct answer
- Wrong Features:Important features which is required by model is missing



###  30-01-2026

Topics Covered:
- Estimator
- fit()
- predict()
- Logistic Regression
- Multi class Regression
- Outliers: These are data points which are different from rest of the data. Read ml.py file for more info



###  2-02-2026

Topics Covered:(In Pandas)
- How to Load Data
- How to Print the data
- How to see basic details of the data
- How to delete the unwanteed rows or columns in the dataframes
- What is Scikit learn Basics also just intro
- How to load a model and how to split the data for training and testing and how to fit the data to the model and how to make predictions with the trained model.


###  3-02-2026

Topics Covered:(Model Evaluation metrics)
- Accuracy
- Precision
- recall
- F1-Score
- Confusion Matrix
- ROC curve basics



###  10-02-2026

Topics Covered: When to use which model for evaluation

Used When:
- Used according to data set
- Used according to the error tolerance factor

Key idea:

START
 |
 |-- Output is number → Regression
 |
 |-- Output is category → Classification
        |
        |-- Simple + explainable → Logistic Regression
        |
        |-- Rules based → Decision Tree
        |
        |-- Strong baseline → Random Forest
        |
        |-- Best accuracy → Gradient Boost / XGBoost


See the practise thing for more info.