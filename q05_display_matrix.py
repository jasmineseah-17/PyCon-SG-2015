
# Displaying matrix of 0s and 1s
import random

a = []

def print_matrix(n):
    line = ""
    for item in range(1, pow(n, 2) + 1):
        a.append(random.randint(0, 1))
    for item in range(len(a)):
        line = line + str(a[item]) + " "
        if (item + 1) % n == 0:
            line += "\n"
    print(line)

x = int(input("Enter number: "))
print_matrix(x)