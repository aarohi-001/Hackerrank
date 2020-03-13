#!/bin/python3

import sys

def solve(grades):
    le=len(grades)
    for i in range(le):
        if(grades[i]>37):
            m=grades[i]%5
            if((5-m)<3):
                grades[i]=grades[i]+(5-m)
    return(grades)   
            
            

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
