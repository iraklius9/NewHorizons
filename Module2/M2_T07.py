hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

t = hour * 60 + mins + dura
print("End time: ", t // 60 % 24, ":", t % 60)
print(t)
