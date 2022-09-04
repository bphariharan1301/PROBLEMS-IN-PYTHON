def conistent_arr(arr, n):
    for i in range(1, n):
        if arr[0] in arr[i]:
            return("No, there is a collision with {}".format(arr[0]))
    return("Yes, the list of {} numbers is consistent".format(n))


n = int(input())

lst = [str(input()) for _ in range(n)]
print(conistent_arr(lst, n))
