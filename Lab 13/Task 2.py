# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:50:41 2021

@author: Dell
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import pytictoc as pt

t=pt.TicToc()
X,Y = make_blobs(n_samples = 500, centers = 5, random_state = 0, cluster_std = 0.5)

for N in range(5,8):
    print("\nFor N: ",N)
    t.tic()
    clustering = AgglomerativeClustering(n_clusters=N,affinity='euclidean',linkage='single')
    clustering.fit_predict(X)
    labels = clustering.labels_
    print("Labels for Single Linkages: \n",labels)
    t.toc()
    
    
    plt.figure()
    plt.scatter(X[:,0],X[:,1], c=labels, cmap='rainbow')
    plt.title("Single Linkage") 
    
    t.tic()
    clustering = AgglomerativeClustering(n_clusters=N,affinity='euclidean',linkage='complete')
    clustering.fit_predict(X)
    labels = clustering.labels_
    print("\nLabels for Complete Linkages: \n",labels)
    t.toc()
    
    plt.figure()
    plt.scatter(X[:,0],X[:,1], c=labels, cmap='rainbow')
    plt.title("Complete Linkage")
    