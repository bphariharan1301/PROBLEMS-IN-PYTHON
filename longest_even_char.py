from collections import Counter


def evenChar(arr):
    res, count = Counter(arr), 0
    for i in res.values():
        if i % 2 == 0:
            count += 1

    return count


arr = list(map(str, input().split()))

print(evenChar(arr))
