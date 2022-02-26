# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:17:17 2021

@author: Dell
"""


from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X,Y = make_blobs(n_samples = 400, centers = 4, random_state = 0, cluster_std = 0.5)
kmeans = KMeans(n_clusters=5, random_state = 0).fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_

plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.title("Unclustered Data") 

plt.figure()
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
plt.scatter(centers[:,0], centers[:,1], color=['lime'], marker='s', linewidth=3)
plt.title("Clustered Data") 

