def digit_of_life():
    n = input("Enter your birthday in the format YYYYMMDD: ")
    while len(n) > 1:
        n = str(sum([int(i) for i in n]))
    return n


print(digit_of_life())
