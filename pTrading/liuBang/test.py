# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:20:15 2017

@author: Hpeng
"""

def aaa(a,b):
    print (a)
    print (b)
def bbb():
    return (1,(12,23))

a,b = bbb()
print (a)
aaa(*b)