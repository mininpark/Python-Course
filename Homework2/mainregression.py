
import pandas as pd
import numpy as np
from scipy import stats

def Regression(X,y):
    # in numpy, np.inv is marix inverse, .T is transpose, @ is matrix multiplication
    XT = X.T
    inverse = np.linalg.inv(XT @ X) 
    beta_hat = inverse @ XT @ y
    e = y - (X @ beta_hat) # error term
    sigma2 = (e.T @ e)/(X.shape[0]-X.shape[1])
    var = np.diag(sigma2 * inverse) # variance
    SE = np.sqrt(var).flatten() #standard error
    t = stats.t.ppf(.975, (X.shape[0] - X.shape[1])) 
    plus = beta_hat + SE * t 
    minus = beta_hat - SE * t 
    # confidence array
    CI = np.hstack([minus, plus]) 
    output = pd.DataFrame(np.hstack([beta_hat, SE, CI]), columns=['Coefficients', 'Standard Error', 'CI-', 'CI+']) 