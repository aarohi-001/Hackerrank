#!/bin/python3

import sys

def getRecord(s):
    lm=[0,0]
    smax=s[0]
    smin=s[0]
    for i in range(1,len(s)):
        if(s[i]>smax):
            smax=s[i]
            lm[0]=lm[0]+1
        if(s[i]<smin):
            smin=s[i]
            lm[1]=lm[1]+1
    return(lm)  

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
