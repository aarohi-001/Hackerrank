#!/bin/python3

import sys

def solve(year):
    if(year>=1700 and year<=1917):
        if(year%4==0):
            dd=12
        else:
            dd=13
    elif(year>=1919 and year<=2700):
        if((year%400==0) or (year%4==0 and year%100!=0)):
            dd=12
        else:
            dd=13
    else:
        if(year==1918):
            dd=26
    mm=9
    return((str(dd)+".0"+str(mm)+"."+str(year)))       
    
            
            
            

year = int(input().strip())
result = solve(year)
print(result)
