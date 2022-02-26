# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:55:09 2021

@author: Dell
"""

str1 = input('Enter some text: ')
strList = str1.split()
size = len(strList)
i = 0
while i < size:
    a = strList[i]
    a.lower()
    if a[0] == 'a' or a[0] == 'e' or a[0] == 'i' or a[0] == 'o' or a[0] == 'u':
        print(strList[i] + ' = ' + a + 'hay')
    else:
        a = a + a[0] + 'ay'
        print(strList[i] + ' = ' + a[1:])
    i+=1