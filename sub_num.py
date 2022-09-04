
# import math


# def SubNum(n1, n2):
#     if n2 in n1:
#         return('YES')
#     else:
#         return('NO')


# n1 = input()
# n2 = input()

# print(SubNum(n1, n2))


n1, n2 = map(int, input().split())
# print(n1, n2)
pv = 1
flag = 0
while(n2//pv):
    pv *= 10
while n1:
    dig = n1 % pv
    # print(dig)
    if dig == n2:
        flag = 1
        break

    n1 //= 10

if flag:
    print('YES')
else:
    print('NO')
