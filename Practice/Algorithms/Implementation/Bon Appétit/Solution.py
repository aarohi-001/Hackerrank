#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    c=ar[k]
    ar[k]=0
    s=sum(ar)
    ba=s//2
    if((ba-b)!=0):
        return((b-ba))
    else:
        return('Bon Appetit')

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
