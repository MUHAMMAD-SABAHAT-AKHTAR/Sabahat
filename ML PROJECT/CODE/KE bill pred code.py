# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 01:31:49 2020

@author: Hewlet Packard
"""


"""
Created on Mon Mar  9 23:16:26 2020

@author: Hewlet Packard
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('20yrs k electric dataset.csv')

#creating array of dataset and variables
m=[1,2,3,4,5,6,7,8,9,10,11,12]



for x in range(1,13):
    a = dataset.iloc[:,0:1].values
    b = dataset.iloc[:,x:x+1].values
  
  

# Splitting the dataset into the Training set and Test set
    """from sklearn.mode import train_test_split
    a_train, a_test, b_train, b_test = train_test_split(a, b, test_size = 0.2, random_state = 0)"""


# Fitting Linear Regression to the dataset
    from sklearn.linear_model import LinearRegression
    lin_reg1 = LinearRegression()
    lin_reg1.fit(a, b)

# Fitting Polynomial Regression to the dataset
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree = 4)
    a_poly = poly_reg.fit_transform(a)
    poly_reg.fit(a_poly, b)
    poly_reg1 = LinearRegression()
    poly_reg1.fit(a_poly, b)

    # Visualising the Linear Regression results
    plt.scatter(a, b, color = 'red')
    plt.plot(a, lin_reg1.predict(a), color = 'blue')
    plt.title(f"MONTH OF {dataset.iloc[:,x:x+1].columns[0] }")
    plt.xlabel('YEARS')
    plt.ylabel('K ELECTTRIC BILLS')
    plt.show()
    
    # Visualising the Polynomial Regression results
    plt.scatter(a, b, color = 'red')
    plt.plot(a, poly_reg1.predict(poly_reg.fit_transform(a)), color = 'blue')
    plt.title(f'MONTH OF {dataset.iloc[:,x:x+1].columns[0]} (Polynomial Regression)')
    plt.xlabel('YEARS')
    plt.ylabel('K ELECTRIC BILLS')
    plt.show()
    
    # Visualising the Polynomial Regression results (for higher resolution and smoother curve)
    a_grid = np.arange(min(a), max(a), 0.1)
    a_grid = a_grid.reshape((len(a_grid), 1))
    plt.scatter(a, b, color = 'red')
    plt.plot(a_grid, poly_reg1.predict(poly_reg.fit_transform(a_grid)), color = 'blue')
    plt.title(f'MONTH OF {dataset.iloc[:,x:x+1].columns[0]} (Polynomial Regression)')
    plt.xlabel('YEARS')
    plt.ylabel('K ELECTRIC BILLS')
    plt.show()

# Predicting a new result with Linear Regression
    print(f"k electric bill of month {dataset.iloc[:,x:x+1].columns[0]}")
    print (lin_reg1.predict([[2016]]))
    
# Predicting a new result with Polynomial Regression
    print(f"k electric bill of month {dataset.iloc[:,x:x+1].columns[0]} (poly reg)")
    print(poly_reg1.predict(poly_reg.fit_transform([[2016]])))
    
#error ratio ####
 
    from sklearn import metrics 
    print('Mean Absolute Error:', metrics.mean_absolute_error(a ,b))
    print('Mean Square Error:', metrics.mean_squared_error(a ,b))
    print('Root Mean Square Error:', np.sqrt(metrics.mean_squared_error(a ,b)))
