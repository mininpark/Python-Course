import pandas as pd
import numpy as np
from scipy import linalg, stats

import pandas as pd


class LinearRegressor:
    def __init__(self):
        self.w_ = None #Regression coefficient value
        self.coef_table = pd.DataFrame() #Table
    
    def _coefficientTable(self, designX, y):
        predictions = np.dot(designX, self.w_)
        MSE = (sum((y-predictions)**2))/(len(designX)-len(designX[0])) #for getting MSE
        var_b = MSE*(np.linalg.inv(np.dot(designX.T,designX)).diagonal())
        se_b = np.sqrt(var_b) 
        ts_b = self.w_.flatten()/ se_b
        p_values =[2*(1-stats.t.cdf(np.abs(i),(len(designX)-len(designX[0])))) for i in ts_b]
        self.coef_table["Coefficients"] = self.w_.flatten()
        self.coef_table["Standard Errors"] = se_b
        self.coef_table["t values"] = ts_b
        self.coef_table["p values"] = p_values
   

    def fit(self, X, y):
        designX = np.c_[np.ones(X.shape[0]), X]
        A = np.dot(designX.T, designX)
        b = np.dot(designX.T, y)
        self.w_ = linalg.solve(A, b) #Regression coefficient value
        
        #coefficient Table
        self._coefficientTable(designX, y)
    
    def predict(self, X):
        if self.w_ is None:
            raise Exception("Please train your datas with 'fit'")
        if X.ndim ==1:
            X = X.reshape(1, -1)
        designX = np.c_[np.ones(X.shape[0]), X]
        return np.dot(designX, self.w_)