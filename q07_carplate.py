entered_carplate = input("Please enter car plate number: ")
carplate = entered_carplate

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

checksum_alphabets = 'AYUSPLJGDBZXTRMKHEC'

checksum = None
if carplate[-1] in alphabets:  # checking if last alphabet entered
    checksum = carplate[-1]
    carplate = carplate[:-1]

if carplate[2] in alphabets:  # checking if 3 alphabets at front
    carplate = carplate[1:]

if len(carplate) == 5:  # checking if only 3 numbers entered
    new_num = []
    for x in range(2):
        new_num.append(carplate[x])
    new_num.append('0')
    for x in range(2, 5):
        new_num.append(carplate[x])

    carplate = ''
    for char in new_num:  # forming new carplate number with 0 appended
        carplate += char

total = 0
weights = [14, 2, 12, 2, 11, 1]
for index in range(6):
    if carplate[index] in alphabets:
        for alphabet in range(26):
            if alphabets[alphabet] == carplate[index]:
                break
        alphabet += 1

        total += (alphabet * weights[index])
    else:
        total += (int(carplate[index]) * weights[index])

correct_checksum = checksum_alphabets[total % 19]

if checksum is None:
    print("The checksum alphabet of the entered car plate number is %s." % correct_checksum)
    print("The completed car plate number is %s%s." % (entered_carplate, correct_checksum))
else:
    if checksum == correct_checksum:
        print("Entered car plate number", entered_carplate, "is VALID.")
    else:
        print("Entered car plate number, %s, is INVALID." % entered_carplate)
        print("Correct checksum alphabet should be %s." % correct_checksum)
        print("Correct car plate number should be %s%s." % (carplate, correct_checksum))

        f = open('INVALID.dat', 'a')
        f.write(entered_carplate + '\n')
        f.close()
