def MaxSum(arr):
    listmax = []
    for number in arr:
        if number > min(arr):
            listmax.append(number)
    maxnum = sum(listmax)
    print(maxnum)


n, t = map(int, input().split())

arr = list(map(int, input().split()))
time = list(map(int, input().split()))
MaxSum(arr)
