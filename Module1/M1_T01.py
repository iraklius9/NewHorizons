# with for loop

for i in range(1, 11):
    print(f"Hello World! {i}")

# with while loop

x = 1
while x < 11:
    print(f"Hello World! {x}")
    x += 1


# with recursion

def hello_world(y):
    if y < 11:
        print(f"Hello World! {y}")
        hello_world(y + 1)


hello_world(1)
