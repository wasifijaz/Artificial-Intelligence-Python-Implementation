# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:13:25 2021

@author: Dell
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pytictoc as tp

t = tp.TicToc()

iris = load_iris()
X = iris.data
Y = iris.target

t.tic()
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.70,random_state=42)
kmeans = KMeans(n_clusters=2, random_state = 0).fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_
Y_pred = kmeans.predict(X_test)
t.toc()

plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.title("Unclustered Data") 

plt.figure()
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
plt.scatter(centers[:,0], centers[:,1], color=['lime'], marker='s', linewidth=3)
plt.title("Clustered Data") 

accuracy = accuracy_score(Y_pred,Y_test)

print("Accuracy: ",accuracy)
