
# Displaying patterns

def display_patterns(n):
    for i in range(1, n + 1):
        total = ""
        for j in range(i, 0, -1):
            total += str(j)
            if n < 10:
                x = (n - i) * " "
            else:
                if i < 10:
                    y = (n - 9) * 2 + 9
                    x = (y - i) * " "
                else:
                    y = (n - 9) * 2
                    z = (i - 9) * 2
                    x = (y - z) * " "
        print(x, total)

x = int(input("Enter number: "))
display_patterns(x)