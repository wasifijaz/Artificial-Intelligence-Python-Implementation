# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:57:23 2021

@author: Student
"""
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score 

X = [[1, 0, 0], [1, 0, 1], [1, 1, 0],[1, 1, 1]]  
y = [1, 1, 1, 0]

clf = MLPClassifier(solver='lbfgs', alpha=0.1,hidden_layer_sizes=(10,4,2), random_state=0) 
clf.fit(X, y) 
 
y_pred= clf.predict([[1,1,1], [2,1,5],[-1,-6,10],[1,0,1]])
print(y_pred)
accuracy = accuracy_score(y_pred,y) 
print(accuracy) 
 