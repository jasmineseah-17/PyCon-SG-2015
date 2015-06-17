
# Finding the largest n such that n3 < 12000

n = 1

while pow(n, 3) < 12000:
    n += 1
    if pow(n, 3) > 12000:
        break
print(n - 1)