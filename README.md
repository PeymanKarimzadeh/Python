# Python-Bisection
"""
@author: Peyman Karimzadeh
"""
def bisection_Method (F, a, b, N_Iterations):
    for iteration in range (1,N_Iterations+1):
        mid=(a+b)/2
    
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
# This is an example
f= lambda x: -x+5
lower_limit=0
Upper_limit=22
number_of_Iterations=122

#bisection_Method(f,lower_limit,Upper_limit,number_of_Iterations)

c=bisection_Method(f,lower_limit,Upper_limit,number_of_Iterations)
