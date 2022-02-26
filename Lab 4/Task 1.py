# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:15:58 2021

@author: Dell
"""

import numpy as np

evenNums = np.arange(0,50,2)
evenNums = evenNums[0:20]
print("First 20 even number in 0 to 50 range: ", evenNums)

oddNums = np.arange(1,50,2)
oddNums = oddNums[0:20]
print("First 20 odd number in 0 to 50 range: ", oddNums)

vecSum = np.add(evenNums, oddNums)
print("Sum of both Vectors: ", vecSum)

print("Maximum number in resultant vector: ", np.amax(vecSum), " and its index: ", np.argmax(vecSum))

print("Minimum number in resultant vector: ", np.amin(vecSum), " and its index: ", np.argmin(vecSum))
