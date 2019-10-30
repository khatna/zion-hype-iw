import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

NUM_COLS = 14

# PREPARING DATA --------------------------------------------------------------

# Loading data as Pandas dataframe
df = pd.read_csv('data.csv', header = 0)
df = df._get_numeric_data()
headers = list(df.columns)
dataset = df.to_numpy()
print(dataset.shape)

# Separate data into features and target
x = dataset[:, 0:NUM_COLS-2]
y = dataset[:, NUM_COLS-2]

# FEATURE SELECTION AND LOGISTIC REGRESSION -----------------------------------

model = LogisticRegression(solver='liblinear')

#Initializing RFE model
rfe = RFE(model, 6)

#Transforming data using RFE
x_rfe = rfe.fit_transform(x,y)  

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x_rfe, y, test_size=0.25, 
random_state=0)

#Fitting the data to model
model.fit(x_train,y_train)

print(rfe.support_)
print(rfe.ranking_)
print(headers)
print(model.score(x_test, y_test))