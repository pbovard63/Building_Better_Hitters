import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV, ElasticNetCV
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import KFold

def mae(y_true, y_pred):
    return np.mean(np.abs(y_pred - y_true))

def lasso_polynomial_lr(X,y):
    '''
    Argument: takes in a set of features X and a target variable y.
    Returns: Performs Lasso polynomial linear regression and returns the feature coefficeints and validation R^2.
    '''

    #Split data from train_val_split
    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=.2, random_state=5)
    
    p = PolynomialFeatures(degree=2)
    X_train_val_poly = p.fit_transform(X_train_val)
    
    s = StandardScaler(with_mean=False)
    X_train_val_poly_scaled = s.fit_transform(X_train_val_poly)
    
    lasso_model = LassoCV(cv= 5)
    lasso_model.fit(X_train_val_poly_scaled , y_train_val)
    lasso_poly_score = lasso_model.score(X_train_val_poly_scaled, y_train_val)
    
    train_val_pred = lasso_model.predict(X_train_val_poly_scaled)
    lasso_mae = mae(y_train_val, train_val_pred)
    #lasso_r2 = r2_score(y_train_val, train_val_pred)
    print('Lasso Linear Regression w/ CV Results:')
    print('Lasso R^2: {}'.format(lasso_poly_score))
    print('Lasso mae: {}'.format(lasso_mae))
    print('Lasso Coefficients: {}'.format(list(zip(p.get_feature_names(), lasso_model.coef_))))