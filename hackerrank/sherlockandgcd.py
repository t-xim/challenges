# https://www.hackerrank.com/contests/coding-challenge/challenges/sherlock-and-gcd/problem

# Single case of runtime error
import math

def solve(a):
    n1 = a[0]
    n2 = a[1]
    gcd = math.gcd(n1, n2)
    for i in range(2, len(a)):
        gcd = math.gcd(gcd, a[i])
    if gcd != 1:
        return "NO"
    else:
        return "YES"
            
    
t = input()

for i in range(int(t)):
    n = input().split()
    a = [int(i) for i in input().split()]

    solution = solve(a)
    print(solution)
