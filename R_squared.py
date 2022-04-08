import numpy as np
import pandas as pd
from functions import linear, quadratic, exponential, Gaussian

def R_squared(fname, function, param1, param2, param3):
    # Calculates R squared value of analytic fit to data
    # fname: name of .csv file where data is stored
    # function: choose between "linear", "quadratic", "exponential" and "Gaussian"
    # param1:
    # param2:
    # param3:
    
    # Load x and y data from .csv file
    data = pd.read_csv(fname+".csv", header=None).to_numpy()
    x_values = data[:,0]
    y_values = data[:,1]

    # Choose analytic function to compare to data
    if function == "linear":
        y_fitted = linear(x=x_values, m=param1, c=param2)
    elif function == "quadratic":
        y_fitted = quadratic(x=x_values, a=param1, b=param2, c=param3)
    elif function == "exponential":
        y_fitted = exponential(x=x_values, A=param1, k=param2, c=param3)
    elif function == "Gaussian":
        y_fitted = Gaussian(x=x_values, A=param1, mu=param2, sigma=param3)
    else:
        print("The function you selected has not been implemented yet!")
    
    # Calculate R squared value
    RSS = 0
    TSS = 0
    mean = np.mean(y_values)
    for i in range(np.size(y_values)):
        RSS = RSS + (y_values[i] - y_fitted[i]) ** 2
        TSS = TSS + (y_values[i] - mean) ** 2
    R_squared = 1 - RSS / TSS
    return R_squared