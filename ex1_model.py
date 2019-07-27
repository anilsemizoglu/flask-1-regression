import pandas as pd
import numpy as np
import pickle

def compute_cost(X, y, theta):
    temp = np.dot(X, theta) - y
    return np.sum(np.power(temp, 2)) / (2*m)

def gradient_descent(X,y,theta,alpha,iterations):
    X_trans = X.transpose()
    gradient_ = []
    gradient2_ = []
    mse = []
    for i in range(iterations):
        prediction = np.dot(X, theta)
        error = prediction-y

        mean_squared_error = np.sum((error) ** 2) / (2 * m)
        mse.append(mean_squared_error)
        # avg gradient per example
        gradient = np.dot(X_trans, error) / m
        gradient_.append(gradient[0])
        gradient2_.append(gradient[1])
        # update
        theta = theta - alpha * gradient
    return theta,gradient_,gradient2_,mse

def predict_function(x,slope,intercept):
    return slope * x + intercept

data1 = pd.read_csv('data/ex1data1.txt',header=None)
x = data1.iloc[:,0]
y = data1.iloc[:,1]
x=np.array(x).reshape(-1,1)
y=np.array(y).reshape(-1,1)
m = x.size
X = np.hstack((np.ones((m,1)), x))
theta = np.zeros([2,1])
iterations = 15000
alpha = 0.01

theta,gradient_,gradient2_,mse = gradient_descent(X,y,theta,alpha,1500)

slope = theta.transpose()[0][1]
intercept = theta.transpose()[0][0]

pickle.dump([slope,intercept], open('models/ex1_restaurant_model.pkl','wb'))
