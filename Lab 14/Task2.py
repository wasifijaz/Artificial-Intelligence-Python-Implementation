# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:14:15 2021

@author: Student
"""

from sklearn.datasets import load_breast_cancer 
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score 
# Loading data 
cancerData = load_breast_cancer() 
 
# Create feature and target arrays 
X = cancerData.data 
y = cancerData.target 
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42) 
 
clf = MLPClassifier() 
clf = MLPClassifier(hidden_layer_sizes=(10,8,6,4,2),max_iter=2000) 
clf = clf.fit(X_train,y_train) 
y_pred = clf.predict(X_test) 

print(y_pred)
accuracy = accuracy_score(y_pred,y_test) 
print(accuracy) 
 