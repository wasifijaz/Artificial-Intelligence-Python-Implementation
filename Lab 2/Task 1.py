# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:22:25 2021

@author: Dell
"""

def menu ():
    print("****** SIMPLE CALCULATOR ******")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    op = int(input("Choose your operator: "))
    return op

def addition (num1, num2):
    out = num1+num2
    return out

def subtraction (num1, num2):
    out = num1-num2
    return out

def division (num1, num2):
    out = num1/num2
    return out

def multiplication (num1, num2):
    out = num1*num2
    return out

op = menu()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if op == 1:
    out = addition(num1, num2)
elif op == 2:
    out = subtraction(num1, num2)
elif op == 3:
    out = division(num1, num2)
elif op == 4:
    out = multiplication(num1, num2)
else: print("Please enter a valid operator...")

print(out)
    
    
    