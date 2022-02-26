# -*- coding: utf-8 -*-
"""
Created on Fri May 28 23:18:34 2021

@author: Dell
"""

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

x = [[25, 40000], [35, 60000], [45, 80000], [20, 20000], [35, 120000], [52, 18000], [23, 95000], [40, 62000], [60, 100000], [48, 220000], [33, 150000]]
y = ['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)

clf = GaussianNB()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print('\ny_predict: ', y_pred)
print("\nAccuracy is ",accuracy)
print('\nConfusion Matrix: \n', confusion_matrix(y_test, y_pred))
