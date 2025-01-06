def read_int(prompt, min_num, max_num):
    while True:
        try:
            v = int(input(prompt))
            assert min_num <= v <= max_num
            return v
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (", min_num, "..", max_num, ")")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
