from mainregression import Regression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv(r"C:\Users\admin\Desktop\Programming\CODE\Python\übung\Homework2\winequality-red.csv", sep=";")

data.dropna(inplace=True) # drop missing values
X = X = data.iloc[:,0:11].values
print(X)
Y = data.iloc[:,-1].values
print (Y)
