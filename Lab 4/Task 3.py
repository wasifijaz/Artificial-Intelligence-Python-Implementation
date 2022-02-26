# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:42:51 2021

@author: Dell
"""

import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])

vecProd = np.multiply(A,B)
print("\nA x B = \n", vecProd)

vecProdM = np.dot(A, B)
print("\nA x B (Matrix Multiplication) = \n", vecProdM)

vecMul = np.matmul(A,B)
print("\nA x B = \n", vecMul)