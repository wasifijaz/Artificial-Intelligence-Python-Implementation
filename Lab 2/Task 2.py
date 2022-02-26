# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:52:34 2021

@author: Dell
"""

a = 1
b = 0
out = 0
nterms = int(input("Enter a positive number: "))
if nterms < 0:
    print("Invalid input value!")
elif nterms == 0:
    print("0")
else:
    print(a)
    i = 0
    while i < nterms - 1:
        out = a + b
        b = out - b
        a = out
        print(out)
        i+=1