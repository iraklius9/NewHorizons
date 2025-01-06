def power_table():
    for x in range(1, 16):
        print(
            f"{x:<3}  *   {x:<3} =   {x ** 2:<6} |"
            f"   {x:<3}  ^   10   =   {x ** 10:<15} |"
            f"   {x:<3}  ^   {x:<3}   =   {x ** x}")


power_table()
