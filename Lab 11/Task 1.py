# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 21:46:13 2021

@author: Dell
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

cancer = load_breast_cancer()
X = cancer.data
Y = cancer.target

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20,random_state=21)

plt.scatter(X_train[:,0], X_train[:,1], c = Y_train, cmap = 'winter')
svc = SVC(kernel='linear').fit(X_train,Y_train)

ax = plt.gca()
xlim = ax.get_xlim()
ax.scatter(X_test[:,0], X_test[:,1], c = Y_test, cmap = 'winter', marker = 'P')

w = svc.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(xlim[0],xlim[1])
yy = a * xx - (svc.intercept_[0] / w[1])

plt.plot(xx,yy)
plt.show()

Y_pred = svc.predict(X_test)
accuracy = accuracy_score(Y_pred,Y_test)
cmat = confusion_matrix(Y_test, Y_pred)

print("Accuracy: ",accuracy)
print('\nConfusion Matrix: \n',cmat)
