'''
Given a positive integer count the values between n1 and n2 (both inclusive) which has unique digits.

Sample I/P:
n1 = 10
n2 = 15

O/P:
5
'''


def printUniqueVal(n1, n2):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    for i in range(n1, n2+1):
        for ind in range(len(arr)):
            arr[ind] = 0
        temp = i
        while(i):
            dig = int(i % 10)
            if (arr[dig] == 1):
                break
            arr[dig] = 1
            i //= 10
        if i == 0:
            # print(temp, end=' ') "Use if asked to print"
            count += 1  # Use if asked to count
        i = temp
    print(count)


n1, n2 = map(int, input().split())

printUniqueVal(n1, n2)
