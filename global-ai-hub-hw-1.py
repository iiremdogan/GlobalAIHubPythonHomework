# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:16:08 2020

@author: iremdogan
"""

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = 5
  
# iterating till the range 
for i in range(0, n): 
    inp = int(input()) 
    lst.append(inp) # adding the element 
      
print(('{} '*len(lst)).format(*lst)) #print all values in the list