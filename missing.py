
from traceback import print_tb


def missing_num(arr, n):
    s = set(i for i in range(1, n+1))
    temp = set(arr)
    return(set(s.difference(temp)))


arr = list(map(int, input().split()))
n = int(input())
print(" ".join(str(i) for i in missing_num(arr, n)), sep=' ')
