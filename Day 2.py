
from collections import Counter

test_str = input('Given Word: ')

print('Given Word is: ' + test_str)

res = Counter(test_str)

res = max(res, key = res.get)

print('Character that occurs the most is: ' + str(res))