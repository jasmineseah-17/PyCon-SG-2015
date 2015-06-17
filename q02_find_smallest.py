
# Finding the smallest n such that n2 > 12000

n = 1

while pow(n, 2) < 12001:
    n += 1
print(n)
