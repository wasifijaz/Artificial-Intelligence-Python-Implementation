# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 11:38:36 2021

@author: Dell
"""

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

X,Y = make_blobs(n_samples = 400, centers = 2, random_state = 0, cluster_std = 0.5)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 21, test_size = 20)

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

print("Y-Prediction: ",Y_pred)
print("Accuracy: ",accuracy)
