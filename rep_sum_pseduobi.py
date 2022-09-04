

def rep_sum_pseduobin(n):
    pv = 1
    cons = 0
    while(n):
        pv = 1
        cons = 0
        dig = 0
        while(int(n/pv)):
            dig = (n/pv) % 10
            if dig > 0:
                cons = 1 * pv + cons
            else:
                cons = 0*pv+cons
            pv = pv*10
            # n /= 10
        print(n, ' ', cons)
        n = n - cons


n = int(input('Enter the num: '))

rep_sum_pseduobin(n)
