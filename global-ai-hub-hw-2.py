# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:37:27 2020

@author: iremdogan
"""

user_info = []

for i in range(4):
    if i == 0:
        print("First Name: ")
    elif i == 1:
        print("Last Name: ")
    elif i == 2:
        print("Age: ")
    elif i == 3:
        print("Birth Year: ")
        
    user_info.append(input())
    
listToStr = ' '.join(map(str, user_info)) 
print(listToStr)  

if int(user_info[2]) < 18:
    print("You can't go out because it is too dangerous")
else :
    print("You can go out to the street")