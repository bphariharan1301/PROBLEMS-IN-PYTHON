def getMaximumGreyness(pixels):

    l = []
    for i in range(len(pixels)):
        l.append(list(map(int, pixels[i])))
    row_1 = []
    for i in range(len(l)):
        k = sum(l[i])
        row_1.append(k)
    col_1 = []
    for i in range(len(l[0])):
        c = 0
        for j in range(len(l)):
            c += l[j][i]
        col_1.append(c)
    m = len(l)
    n = len(l[0])
    ans = [[0]*n]*m
    res = -float("inf")
    for i in range(len(l)):
        for j in range(len(l[0])):
            x = row_1[i]
            y = col_1[j]
            ans[i][j] = 2*(x+y)-(m+n)
            res = max(res, ans[i][j])
    return res


pixels = ["011", "101", "001"]
print(getMaximumGreyness(pixels))
