# -*- coding: utf-8 -*-
"""
Created on Fri May 28 23:34:59 2021

@author: Dell
"""

from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

ds = load_breast_cancer()

x = ds.data
y = ds.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

clf = GaussianNB()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print('\ny_predict: ', y_pred)
print("\nAccuracy is ",accuracy)
print('\nConfusion Matrix: \n', confusion_matrix(y_test, y_pred))
