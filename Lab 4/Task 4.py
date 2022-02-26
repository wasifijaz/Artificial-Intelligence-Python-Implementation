# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:47:19 2021

@author: Dell
"""

import numpy as np

A = np.ones([2,2], dtype = int)
print("A = \n", A)

B = np.zeros([2,2], dtype = int)
print("B = \n", B)

conHor = np.concatenate((A,B), axis=1)
print("\nHorizontal concatenation = \n", conHor, "\nShape = ", np.shape(conHor))

conVer = np.concatenate((A,B), axis=0)
print("\nVertical concatenation = \n", conVer, "\nShape = ", np.shape(conVer))

con = np.dstack((A,B))
print("\nDStack concatenation = \n", con, "\nShape = ", np.shape(con))

fla = con.flatten()
print("\nFlatten Resultant = \n", fla, "\nShape = ", np.shape(fla))
