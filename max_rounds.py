from collections import Counter
from math import ceil
boxes = [2, 3, 3]


def calMinRounds(boxes):
    res = 0
    cnt = Counter(boxes)
    for v in cnt.values():
        if v == 1:
            return -1
        res += ceil(v / 3)
    return res


print(calMinRounds(boxes))
