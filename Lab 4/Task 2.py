# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:07:53 2021

@author: Dell
"""

import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[5,8,9],[1,3,1],[6,2,4]])
 
vecSum = np.add(A, B)
print("A + B = \n", vecSum)

vecSub = np.subtract(A, B)
print("\nA - B = \n", vecSub)

vecProd = np.multiply(A, B)
print("\nA x B (Element Wise) = \n", vecProd)

vecProdM = np.dot(A, B)
print("\nA x B (Matrix Multiplication) = \n", vecProdM)

vecDiv = np.divide(A, B)
print("\nA / B (Element Wise) = \n", vecDiv)

vecDivInv = np.dot(A, np.linalg.inv(B))
print("\nA / B (Matrix Division using Inverse) = \n", vecDivInv)

print("\nMaximum number in A+B: ", np.amax(vecSum))
print("Maximum number in A-B: ", np.amax(vecSub))

print("\nMinimum number in A+B: ", np.amin(vecSum))
print("Minimum number in A-B: ", np.amin(vecSub))

print("\nMean number in A+B: ", np.mean(vecSum))
print("Mean number in A-B: ", np.mean(vecSub))

print("\nDeterminant of A*B: ", np.linalg.det(vecProdM))

print("\nTranspose of A*B: ", np.transpose(vecProdM))

print("\nTrace of A/B: ", np.trace(vecDivInv))
