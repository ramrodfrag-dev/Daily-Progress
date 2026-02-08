# This contains all the base concepts of ML with examples and understandings
#**** means it is important

#28-01-2026

'''Differnce Between Supervised and UnSupervised Learning'''
'''Supervised Learning:'''
# ->Machine Learning Algorithm is trained on labelled data ->Means it knows for what input what output comes(Given). So, with this it leans patterns and guesses or predicts the output for new input.
# It has 2 sub categories:
# a.Classification: Talks about the output is a discrete label or not ->Means the outcomes are choosen from fiite number of values but not continuous values like 2.8 is cat or dog. only between cat and dog and so,on.
# Ex: Linear classifiers, Random Forests, Decision trees,etc are examples of these type.
# b.Regression: The output here is a continuous value such as prics,probability
# Ex: Linear regression and logical regression are 2 common types.

#It adjusts to the values and learns much better.


'''UnSupervised Learning:'''
# ->It is not given with any labeled data or It does not require labels. so, these find out the hidden patterns in data without the need for human Intervention
# It has 3 sub categories:
# a.CLustering: They goups tasks based on their similarities and so,on. which makes them as a group.
# Ex: People are grouped based on interests they have an what they like.
# b.Association: Here algorithm looks relationship between the variables and data.
# Ex: used in buisiness market analysis like which items have brought together and so,on
# c.Dimensionality Reduction: Here the algorithm tries to reduces the number of variables in the data while preserving the as much information as possible.
# Ex: Used in preprocessing stages like autoencoders remove noise from visual images to improve picture quality

'''
Why Supervised is best?
1.Supervised Learning models tend to be more accurate than unsupervised models.
2.UnSupervised Learning models do not make predictions, they only group the data together. But Supervised can make good predictions.
3.Classifying data is hard but trustworthy

Why UnSupervised is best?
1.Unsupervised Leaning can be used to find hidden patterns which supervised larning models cannot find.
2.It does not need labelled dat which most of our world has
3.Classifying data is easy but it cannot be trusted which it belongs to.
'''


#In order to get both benefits we use other Learning known as Semi-Supervised Learning:
#Semi-Supervised Learning: It uses training dataset of both labelled and unlabelled data. Note:It learns from unlabeled data not just predicts it by labeled data and leave it.
# ->Used when it is difficult to extract features or we have high volumes of data.
# Ex: We can use this when we have millions of images are there but only a few thoudsand are labelled like radiology pics. here it learns and tells which patient needs more medical assistant.
# ****It is ideal for medical images where a small amount of data could leed to significant increase in accuracy.





#30-01-2026

'''Terminolgy of predict,fit,estimator functions in scikit learn'''
# estimator: It is nothing but a model which learns from data and predicts new inputs by some functions
# fit(): It is a function in estimator which can be called like:
# model.fit(X_train, y_train)  ->This makes the model learn from given x,y values.
# predict : It is also a function in estimator which can be called like:
#predictions = model.predict(X_test) ->Here it predicts by taking new x_values 

#Estimators generally train with numerical data and if the data is not numerical also it is converted to numericals with contextual embeddings and then used.

'''Methods USed for classification and Regression Problems:
1. Multiple Linear Regrssion Models for Regression problems where it takes a set of features and their values and produce a real numbers output.
 here softmax activation function is used.
2. Logistic Regression Models for Classifications problems where it takes a bunch of features  and finally produce a binary valued outcomes like 0 or 1.
 here sigmoid activation function is used.
Think of Logistic Regrssion as takin the Linear Regression and squashing it through the logistic function to produce fixed number of outputs.
'''

'''Outliers'''
# Thse are the data points which are different from others and which make the model vulnerable.
#Ex: If the data set is 20,23,35,27,39,34,29,1278 then 1278 is an outlier. since it is there the model thinks the average is much greater and the results will not be accurate.




# 02-02-2026
'''Scikit Learn Basics'''
# Scikit-learn expects the data as a matrix X of features and a vector y of labels, it does not care about file formats, only numerical arrays.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
x,y = load_iris(return_x_y=True)                    #Loading data
x_train,x_test,y_train,y_test = train_test_split(   #Spliting data
    x,y,test_size=0.2,random_state=42
)
model=LogisticRegression()
model.fit(x_train,y_train)                          # Training model
y_pred=model.predict(x_test)                        #Prediction of testing data



'''Pandas Basics '''
# -> It is a python library for data analysis and manipulation. The core object is to work with a DataFrame which is like a spreadsheet or like a database table in python.
# Basics
import pandas as pd
data={"Name":["A","B","C"],"Age":[19,20,21]}  #Random Data
df=pd.read_csv("your_file.csv")         # Use pd.read_exel("yourfile.xlsx")  for loading the excel sheets.
df=pd.DataFrams(data)           # Converts the raw data in to a Dataframe

print(df.head())   # Which prints the first 5 rows of the dataFrames.
# df.head(10)  for 10 rows to come. Do: df.tail() for getting the last rows of dataframes.
print(df.describe())   # shows summary statistics for numeric columns like count,mean,min/max, quartiles
df.isnull().sum()      # This tells how many missing values are there for each column. Is null() checks if it is null or not and then .sum() is used to calculate null elements count.

df.iloc[1:4]  # Gives the values from the rows indexed from 1 to 3 of the dataframe.
df.iloc[1,2]  # Gives the values from 1st row and 2nd column.

threshold = len(df) * 0.5
df = df.dropna(axis=1,thresh=threshold) # Here if the axis is 0 then rows with more than 50 null values will be dropped but here it removes columns which has more than 50 elements null.
df['Column_name']=df['Column_name'].fillna(df['Column_name'].mean()) # Fills all null values with the mean of all the remaining values.

len(df)  # Gives the total number of rows in the dataframe.
df.shape[0] #Gives the total number of rows in df and if we put 1 we get total number of colums. And if we do only the df.shape we get both.
df[df["Rating"]==4] #Prints Rating which are 4 from df
df.sample(10)  #gives any 10 random rows.

df.sort_values(by=["price","Quantity"],ascending=[False,True])
#In the above thing first price will be sorted in Descending order and then in those elements Quantity will be sorted in the Ascending order as that of mentioned.




#03-02-2026

'''ML Model Evaluation Metrics(Fundamental)'''
# Confusion Matrix
'''
Reality/Prediction     spam    Not spam

Actually spam          TP        FN

Acutually not spam     FP        TN
'''

# a.Accuracy: % of correct classified classes (or) How many total predictions were correct. It sees over all correctness. It is correct Predictions by total predictions.
'''(TP+TN)/Total''' #->Formula
# b.Precision: % of how many predicted +ves are actually +ves.
'''TP/(TP+FP)''' #->Formula
# Remember: No good guy should be punished.
#c.Recall: Did I catch all the bad guys
'''TP/(TP+FN)''' #->Formula
#d. F1 Score: It is balance between precision and recall.
# Remember: If one is low among precision and recall then f1 drops hard, so it maintains them. so, we need to use Harmonic Relation to do this.
'''F1=2*(Precision*Recall)/(Precision+Recall)''' #->Formula
#e. ROC Curve: How Brave my model is? Threshhold can be increased or decreased according to results.
# Rememeber: How model behaves when you change strictness, So it is graph depicting it.
#f. AUC: Area under the ROC Curve-> This is the single number summary.
'''AUC=1.0 ->Perfect
      =0.9 ->Excellent
      =0.5 ->Worst
      <0.5 ->Worse than random'''  # Here <0.5 we generally flip the predictions to make it better.
# Remember: How smart the model is? And this is acquired by the area under the curve.


# Also there are other terms named Specificity and sensitivity:
#g. Sensitivity: This is true positivity. Remember +ve is Catching all bad guys
'''TP/(TP+FN)''' #-> Same formula as that of Recall
#f. Specificity: This is true negativity. Remember -ve means opposite of positive so 2 terms came in +ve so, other 2 comes in -ve
'''TN/(TN+FP)''' # -> Remember this formula by thinking true -ve so, it must be opp of +ve.




