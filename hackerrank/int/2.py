# String osc
# 1. alphabet weight means a is smaller than b, begin with smallest char
# 2. sort string ss, begin with smallest alphabet, (larger than prev)
# 3. repeat step 2 until not possible
# 4. get largest char from remaining, that is smaller than prev, append again
# 5. repeat
# 6. if none chosen because all equal, choose any char and append
# 7. repeat until all string done
# E.g.
# s = ababyz
# ss = abyzba
