
# Finding the factors of an integer

def factors(n):
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                yield i
                break # break here so it goes back to while loop instead of for loop

x = int(input("Enter number:"))
print("Factors of", x)
for factor in factors(x):
    print(factor)