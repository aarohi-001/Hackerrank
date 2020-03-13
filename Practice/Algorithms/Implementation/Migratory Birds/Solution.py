#!/bin/python3

import sys

def migratoryBirds(n, ar):
    m=max(ar)
    c=[0]*(m+1)
    for i in ar:
        c[i]=c[i]+1
    mn=max(c)
    return(c.index(mn))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
