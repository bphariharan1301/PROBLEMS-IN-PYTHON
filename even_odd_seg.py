def even_odd_seg():
    pass


n = int(input('ENter Size: '))

arr = list(map(int, input().split()))
print('TYPE: ', type(arr))

for ind in range(0, n):
    while(arr[ind] % 2 == 0):
        ind += 1
    # e_ind = ind+1
    for e_ind in range(ind+1, n and arr[e_ind] % 2 != 0):
        if e_ind >= n:
            break
        safe = arr[e_ind]

        for shift in range(e_ind, shift > ind, -1):
            arr[shift] = arr[shift-1]
        arr[ind] = safe

for i in arr:
    print(i, end=' ')
