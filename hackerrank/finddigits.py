# https://www.hackerrank.com/contests/coding-challenge/challenges/find-digits/problem
# Difficulty: Easy

# Complete the findDigits function below.
def finddigits(n):
    counter = 0
    for i in list(str(n)):
        digit = int(i)
        if (digit != 0) and ((n%digit == 0)):
            counter += 1
    return counter

t = int(input().strip())
for t0 in range(t):
    n = int(input().strip())
    output = finddigits(n)
    print(output)
    
