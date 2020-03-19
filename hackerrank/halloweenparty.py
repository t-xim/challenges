# https://www.hackerrank.com/contests/coding-challenge/challenges/halloween-party/problem
# Difficulty: Easy

import math

# 2 methods of doing it
# 1 is a simple multiplication of a floor of one number and the ceiling of another (half of K)
# using a summation where you add 1 1 2 2 3 3 4 4 etc (floor n/2 + 1 from n = 0+)

# method 1 (Far superior method)
def halloweenparty(k):
    return (math.floor(k/2) * math.ceil(k/2))
    
# method 2
#def halloweenparty(k):
#    n = 0
#    for i in range(k):
#        n += math.floor((i+1)/2)
#    return n
    
t = int(input().strip())
for t0 in range(t):
    k = int(input().strip())
    pieces = halloweenparty(k)
    print(pieces)
