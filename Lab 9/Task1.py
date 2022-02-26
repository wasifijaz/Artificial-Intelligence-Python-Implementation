# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:45:04 2021

@author: Dell
"""
from sklearn.neighbors import KNeighborsClassifier

x_train = [[25, 40000], [35, 60000], [45, 80000], [20, 20000], [35, 120000], [52, 18000], [23, 95000], [40, 62000], [60, 100000], [48, 220000], [33, 150000]]
y_train = ['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']

knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(x_train, y_train)

x_test = [[48, 142000]]

y_pred = knn.predict(x_test)

print('x_test: ',x_test,'\ny_predict: ',y_pred)
