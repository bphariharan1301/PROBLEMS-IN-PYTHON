def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def check_prime_fac(n):
    if(is_prime):
        if (n % 2 == 0) and (n % 3 == 0) and (n % 5 == 0):
            return True
    return False


n = int(input())

if (check_prime_fac):
    print('Yes')
else:
    print('No')
