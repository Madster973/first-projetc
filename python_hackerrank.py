# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:26:19 2019

@author: MADSTER
"""

"""To print the numeric triangle like
1
22
333
4444
for a given input N"""
for i in range(1,int(input())):
    print(((10**i)//9)*i)