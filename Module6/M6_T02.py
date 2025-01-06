digits = [
    [" ### ", "#   #", "#   #", "#   #", " ### "],
    ["  #  ", "  #  ", "  #  ", "  #  ", "  #  "],
    [" ### ", "    #", " ### ", "#    ", " ### "],
    [" ### ", "    #", " ### ", "    #", " ### "],
    ["#   #", "#   #", " ### ", "    #", "    #"],
    ["#### ", "#    ", " ### ", "    #", " ### "],
    [" ### ", "#    ", " ### ", "#   #", " ### "],
    [" ### ", "    #", "    #", "    #", "    #"],
    [" ### ", "#   #", " ### ", "#   #", " ### "],
    [" ### ", "#   #", " ### ", "    #", " ### "],
]

number_str = input("Enter a non-negative integer: ")

output_lines = [""] * 5

for digit in number_str:
    for i in range(5):
        output_lines[i] += digits[int(digit)][i] + " "

for line in output_lines:
    print(line.rstrip())
