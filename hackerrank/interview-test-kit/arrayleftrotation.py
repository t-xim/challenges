# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
# Difficulty Easy

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# Causes runtime error
def rotLeft(a, d):
    for i in range(d):
        holder = a[0]
        for j in range(n-1):
            a[j] = a[j+1]
        a[n-1] = holder  
    return a
    
# Without loops
# def rotLeft(a, d): 
#    b = [] 
#    b = a[d:len(a)] + a[0:d] 
#    return b

nd = input().split()
n = int(nd[0])
d = int(nd[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(" ".join(map(str, result)))
