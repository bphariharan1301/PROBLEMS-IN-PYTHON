def unlockKey(n):
    pass


n = int(input('Enter The Num: '))
cons = 0
cons_pv = 1
for dig in range(1, 10):
    pv = 1
    while int(n/pv):
        r = (n/pv) % 10
        if r == dig:
            cons = cons*10+dig
            cons_pv = cons_pv*10
        pv *= 10

pv /= 10
cons_pv /= 10

print(int((cons/cons_pv)*pv+(cons % cons_pv))+1)
