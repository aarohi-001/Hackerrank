#!/bin/python3

import sys

def solve(n, s, d, m):
    t=0
    for i in range(n-m+1):
        su=sum(s[i:i+m])
        if(su==d):
            t=t+1
    return(t)
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
