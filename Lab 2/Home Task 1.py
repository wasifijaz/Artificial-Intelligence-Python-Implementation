# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:23:04 2021

@author: Dell
"""

students = ['Wasif','Waleed','Ammara','Arhama']
print(students)
students.append('Ahmer')
print(students)
newStudents = ['Basit','Meji','Wasif','Humza']
students.extend(newStudents)
print(students)
students.insert(len(students),'Mubashir')
print(students)
students.remove('Basit')
print(students)
a = students.pop(2)
print(a)
a = students.pop()
print(a)
a = students.count('Wasif')
print(a)
students.sort()
print(students)
students.reverse()
print(students)