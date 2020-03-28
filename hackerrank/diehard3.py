# https://www.hackerrank.com/challenges/die-hard-3/problem
# Practice - medium difficulty

import math

def solve(a, b, c):
    
    if (c > a) and (c > b):
        return "NO"
    
    if c % math.gcd(a,b) == 0:    
        return "YES"
    else:
        return "NO"

t = int(input().strip())

for i in range(int(t)):
    arr = [int(i) for i in input().split()]

    a = arr[0]
    b = arr[1]
    c = arr[2]

    solution = solve(a,b,c)
    print(solution)
