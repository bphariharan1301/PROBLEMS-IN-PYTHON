'''rows = 5
for i in range(0, rows + 1):
    for j in range(rows-i, 0, -1):
        print(j, end=' ')
    print()'''

# print num in rev from 10 to 1
'''start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop'''

# Left rev
'''row = 6
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()'''

# num tri pat
'''rows = 5
for i in range(1, rows+1):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print('*', end=' ')
            num += 1
    print("")'''
# Sq num pat
'''row = 9
for i in range(1,row+1):
    for j in range(1,row+1):
        print(j, end=' ')
    print()'''

# print full pyramids

# rows = int(input("Enter number of rows: "))
# k = 0
# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")

#     while k != (2*i-1):
#         print("* ", end="")
#         k += 1

#     k = 0

#     print()

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")

    while k != (2*i-1):
        print("* ", end="")
        k += 1

    k = 0
    print()
