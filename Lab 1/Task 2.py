# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:52:08 2021

@author: Dell
"""
i = 1
while i == 1:    
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    op = input("Enter operator [+, -, *, /]: ")

    if op == '+':   
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)
    else:
        print('Invalid operator...!')
    
    i = int(input("Enter '1' to contiune calculating: "))
    