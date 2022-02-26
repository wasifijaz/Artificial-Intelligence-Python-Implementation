# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:43:36 2021

@author: Dell
"""

num1 = int(input("Enter a number to calculate Factroial: "))
out = 1 

while num1>0:
    out = out*num1
    num1 = num1-1
    
print(out)