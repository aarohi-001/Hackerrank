#!/bin/python3

import sys
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
total=[]
maxa=max(a)
minb=min(b)
if(maxa<minb):
    for i in range(maxa, minb+1):
        f=0
        g=0
        for j in a:
            if(i%j==0):
                f=f+1
            else:
                break
        for k in b:
            if(k%i==0):
                g=g+1
            else:
                break
        if(f==n and g==m):
            total.append(i)
print(len(total))
