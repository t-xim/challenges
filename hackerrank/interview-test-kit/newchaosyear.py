# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Difficulty Medium

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total = 0
    for i, val in enumerate(q):
        if val-(i+1) > 2:
            return "Too chaotic"
        for j in range(max(val-2,0), i+1):
            if q[j] > val:
                total += 1
                
    return total
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)
        print(result)
