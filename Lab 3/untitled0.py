# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:02:52 2021

@author: Dell
"""
import math 

class basic_calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def addition(self):
        return self.num1+self.num2
    def subtraction(self):
        return self.num1-self.num2
    def division(self):
        return self.num1/self.num2
    def multiplication(self):
        return self.num1*self.num2
  

class s_calc(basic_calc):
    def __init__(self, num3, num4):
        self.num3 = num3
        self.num4 = num4
        super().__init__(num3, num4)
    def factorial(self):
        out = 1 
        while self.num3>0:
            out = out*self.num3
            self.num3 = self.num3-1
        return out
    def x_power_y(self):
        if self.num4 == 0:
            return "1"
        elif self.num4 == 1:
            return self.num3
        elif self.num4 > 1:
            out = self.num3
            while self.num4-1 != 0:
                out = out*self.num3
                self.num4-=1
            return out
    def log_base_2(self):
        return math.log(self.num3,self.num4)
    def natural_log(self):
        return math.log(self.num3)


choice = 1
while choice != 0:    
    print("\n\n****** SELECT CALCULATOR ******\n")
    print("\n1. Basic Calculator")
    print("2. Advanced Calculator")
    print("0. Exit")
    choice = int(input("Choose your Calculator: "))
    if choice == 1:
        op = 1
        while op != 0:
            print("\n\n\t****** BASIC CALCULATOR ******\n")
            num1 = int(input("\t\tEnter first number: "))
            num2 = int(input("\t\tEnter second number: "))
            cal_Obj = basic_calc(num1, num2)
            print("\n\t1. Addition")
            print("\t2. Subtraction")
            print("\t3. Division")
            print("\t4. Multiplication")
            print("\t0. Exit")
            op = int(input("\tChoose your operator: "))
            if op == 1:
                print("\n\t\tResult: ",cal_Obj.addition())
            elif op == 2:
                print("\n\t\tResult: ",cal_Obj.subtraction())
            elif op == 3:
                print("\n\t\tResult: ",cal_Obj.division())
            elif op == 4:
                print("\n\t\tResult: ",cal_Obj.multiplication())
            elif op == 0:
                print("\n\t\tThank You for using Basic Calculator!")
            else: print("\n\t\tPlease enter a valid operator...")
    elif choice == 2:
        op = 1
        while op != 0:
            print("\n\n\t****** ADVANCED CALCULATOR ******\n")
            print("\n\t1. Factorial")
            print("\t2. X_Power_Y")
            print("\t3. Logarithm")
            print("\t4. Natural Logarithm")
            print("\t5. Addition")
            print("\t6. Subtraction")
            print("\t7. Division")
            print("\t8. Multiplication")
            print("\t0. Exit")
            op = int(input("\tChoose your operator: "))
            if op >=5 and op <=8:
                 num3 = int(input("\t\tEnter first number: "))
                 num4 = int(input("\t\tEnter second number: "))
                 cal_Obj = s_calc(num3, num4)
            num4 = 0
            if op == 1:
                num3 = int(input("\tEnter a number to calculate Factroial: "))
                cal_Obj = s_calc(num3, num4)
                print("\n\t\tResult: ",cal_Obj.factorial())
            elif op == 2:
                num3 = int(input("\tEnter base X: "))
                num4 = int(input("\tEnter power Y: "))
                cal_Obj = s_calc(num3, num4)
                print("\n\t\tResult: ",cal_Obj.x_power_y())
            elif op == 3:
                num3 = int(input("\tEnter value: "))
                num4 = int(input("\tEnter base: "))
                cal_Obj = s_calc(num3, num4)
                print("\n\t\tResult: ",cal_Obj.log_base_2())
            elif op == 4:
                num3 = int(input("\tEnter value for Natural Log: "))
                cal_Obj = s_calc(num3, num4)
                print("\n\t\tResult: ",cal_Obj.natural_log())
            elif op == 5:
                print("\n\t\tResult: ",cal_Obj.addition())
            elif op == 6:
                print("\n\t\tResult: ",cal_Obj.subtraction())
            elif op == 7:
                print("\n\t\tResult: ",cal_Obj.division())
            elif op == 8:
                print("\n\t\tResult: ",cal_Obj.multiplication())
            elif op == 0:
                print("\n\t\tThank You for using Advanced Calculator!")
            else: print("\n\t\tPlease enter a valid operator...")
    elif choice == 0:
        print("\n\tThank You for using Calculator!")
    else: print("\n\tPlease enter a valid operator...")
                
