# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:51:04 2019

@author: MADSTER
"""
"""
This is solution to hackerrank problem named Validating and Parsing E-mail ID
We have completed it using Regex Pattern
"""
import re
n = int(input())
pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    x,y = input().split(" ")
    m=re.match(pattern,y)
    if(m):
        print(x,y)
