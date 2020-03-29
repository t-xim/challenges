# https://www.hackerrank.com/challenges/two-strings/problem
# Practice, Difficulty Easy


def twostrings(a, b):
    s1 = set(a)
    s2 = set(b)

    if len(s1.intersection(s2)) > 0:
        return "YES"
    else:
        return "NO"


p = int(input())

for i in range(p):
    word1 = input()
    word2 = input()
    solution = twostrings(word1, word2)
    print(solution)
