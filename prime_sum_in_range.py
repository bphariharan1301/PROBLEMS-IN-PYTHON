import sympy

r = int(input())
sum, count = 2, 0
for i in range(1, r+1):
    if sympy.isprime(i):
        sum += i

        if (sympy.isprime(i) and sum <= r):
            # print(sum)
            count += 1

print('TOTAL COUNT: ', count)
