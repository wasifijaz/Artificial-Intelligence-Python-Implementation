# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:49:17 2021

@author: Dell
"""

import scipy.spatial
from collections import Counter
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.05, random_state = 42)

class KNEAREST:
    def __init__(self, k):
        self.k = k
        
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y
        
    def distance(self, x1, x2):
        distance = scipy.spatial.distance.euclidean(x1, x2)
    
    def predict(self, x_test):
        final_output = []
        for i in range(len(x_test)):
            d = []
            votes = []
            for j in range(len(x_train)):
                dist = scipy.spatial.distance.euclidean(x_train[j] , x_test[i])
                d.append([dist, j])
            d.sort()
            d = d[0:self.k]
            for d, j in d:
                votes.append(y_train[j])
            ans = Counter(votes).most_common(1)[0][0]
            final_output.append(ans)
            
        return final_output
    
    def score(self, x_test, y_test):
        predictions = self.predict(x_test)
        return (predictions == y_test).sum() / len(y_test)
    
classifer = KNEAREST(5)
classifer.fit(x_train, y_train)
prediction = classifer.predict(x_test)
print('\ny_predict: ', prediction)
print('\nAccuracy: ', classifer.score(x_test, y_test))

print('\nConfusion Matrix: \n', confusion_matrix(y_test, prediction))



