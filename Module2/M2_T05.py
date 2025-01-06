a = float(input("Enter a float value for variable a: "))
b = float(input("Enter a float value for variable b: "))

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
try:
    print("a / b = ", a / b)
except ZeroDivisionError:
    print("can't divide by zero")

print("\nThat's all, folks!")
