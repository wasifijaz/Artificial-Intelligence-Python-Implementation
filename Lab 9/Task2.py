# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:14:43 2021

@author: Dell
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

x = [[25, 40000], [35, 60000], [45, 80000], [20, 20000], [35, 120000], [52, 18000], [23, 95000], [40, 62000], [60, 100000], [48, 220000], [33, 150000]]
y = ['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state=42)
accuracy = {}

odd = range(1, 10, 2)

for i in odd:
    if i % 2 != 0: 
        print('\nk = ',i)
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_test)
        print('\tx_test: ',x_test,'\n\ty_predict: ',y_pred)
        test_acc = accuracy_score(y_test, y_pred)
        accuracy[i]=test_acc
        print('\tAccuracy: ',test_acc)

max_key = max(accuracy, key = accuracy.get)
print('\nBest value of k = ',max_key)

print('\n',confusion_matrix(y_test, y_pred))

plt.plot(odd, list(accuracy.values()), label = 'Testing Dataset Accuracy - Task 2')
plt.legend()
plt.xlabel('n_neighbors')
plt.ylabel('Accuracy')
plt.show()