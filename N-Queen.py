
def check(a, i, j):
    for col in range(j, -1, -1):
        if a[i][col] == 1:
            return 0
    col = j
    for row in range(i, n):
        if a[row][col] == 1:
            return 0
        col -= 1
    col = j
    for row in range(i, -1, -1):
        if a[row][col] == 1:
            return 0
    return 1


def queen(a, j):
    if j == n:
        return 1
    else:
        for i in range(n):
            if check(a, i, j):
                a[i][j] = 1
                if queen(a, j+1):
                    return 1
                a[i][j] = 0
        return 0


n = int(input())
# a = [[0, 0] for _ in range(n*n)]
a = [[]]

for i in range(n*n):
    a[0][i] = 0

if queen(a, 0):
    for i in range(n*n):
        print(a[0][1], end=' ')
        if (i+1) % n == 0:
            print("\n")

# for
