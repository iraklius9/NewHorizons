hat_list = [1, 2, 3, 4, 5]

hat_list[int(len(hat_list) / 2)] = int(input("Enter a number to replace the middle number: "))

hat_list.pop()

print(len(hat_list))

print(hat_list)
