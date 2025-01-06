month, year = input("Enter month and year in MM-YYYY format: ").split("-")
month = int(month)
year = int(year)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]

days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

if month < 3:
    month += 12
    year -= 1
k = year % 100
j = year // 100
f = 1 + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j
start_day = f % 7

start_day = (start_day + 5) % 7

print(f"{months[month - 1]} {year}")
print(" ".join(days))

if month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month = 29
    else:
        days_in_month = 28
elif month in [4, 6, 9, 11]:
    days_in_month = 30
else:
    days_in_month = 31

day = 1
for i in range(6):
    for j in range(7):
        if i == 0 and j < start_day:
            print("   ", end="")
        elif day <= days_in_month:
            print(f"{day:2} ", end="")
            day += 1
        else:
            print("   ", end="")
    print()
