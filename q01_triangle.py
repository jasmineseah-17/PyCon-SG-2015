
# Validating triangles and computing perimeter

while True:
    try:
        side1 = int(input("Enter side 1: "))
        side2 = int(input("Enter side 2: "))
        side3 = int(input("Enter side 3: "))
        while not side1 and side2 and side3 > 0:
            side1 = int(input("Please enter positive integer: "))
            side2 = int(input("Please enter positive integer: "))
            side3 = int(input("Please enter positive integer: "))
        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
            sum = side1 + side2 + side3
            print("Perimeter:", sum)
            break
        else:
            print("Triangle is invalid!")
    except ValueError:
        print("Please enter an integer.")