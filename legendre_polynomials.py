

def LegendrePolynomials(n, x):
    if(n == 0):
        return 1  # P0 = 1
    elif(n == 1):
        return x  # P1 = x
    else:
        return (((2 * n)-1)*x * LegendrePolynomials(n-1, x)-(n-1)*LegendrePolynomials(n-2, x))/float(n)


m = int(input())
temp = []
t = []
for i in range(m):
    x, n = float(input()), int(input())
    t.append(x)
    t.append(n)
    temp.append(t)

for i in range(len(temp)):
    j = 0
    # print('i VALUE IS: ', i)
    print(temp[i][j], end=' ')  # Value of x to pass
    print(temp[i][j+1])  # Value of n to pass
    n, x = int(temp[i][j+1]), int(temp[i][j])
    print(LegendrePolynomials(n, x))
# print(LegendrePolynomials(n=2, x=0.5))
