# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:00:37 2021

@author: Student
"""
from sklearn.neural_network import MLPClassifier 

X = [[0., 0.], [1., 1.]]  
y = [0, 1] 

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1) 
clf.fit(X, y) 
 
print(clf.predict([[2., 2.], [-1., -2.]])) 
