# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:05:40 2021
Note:
This is a rudimentary Python code for bisection method.
Note: It is not complete and need to be edited 

@author: Peyman Karimzadeh
"""
def secant_Method (F, a, b, N_Iterations):
    for iteration in range (1,N_Iterations+1):
        mid=a-((a-b)*F(a)/(F(a)-F(b)))
        if mid>b or mid < a:
            print('Wrong limit')
            break
        if F(mid)==0:
            print ("The exact root is:", mid)
            break
        elif F(a)*F(mid)<0:
            b=mid
            a=a    
        elif F(b)*F(mid) <0:
            a=mid
            b=b
        elif F(a)*F(b)>=0:
            print("There is no root or this Method can not dignoise it")
            break
    return mid

f= lambda x: -x+35

lower_limit=0
Upper_limit=22
number_of_Iterations=122

#bisection_Method(f,lower_limit,Upper_limit,number_of_Iterations)

c=secant_Method(f,lower_limit,Upper_limit,number_of_Iterations)

