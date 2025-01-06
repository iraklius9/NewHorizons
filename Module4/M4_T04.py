from M4_T03 import days_in_month


def day_of_year(year, month, day):
    days = 0

    for i in range(1, month):
        days += days_in_month(year, i)

    days += day

    return days


print(day_of_year(2000, 12, 31))
