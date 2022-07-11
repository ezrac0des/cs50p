print("meow")
print("meow")
print("meow")

print("---------------------")

i = 0
while i < 3:
    print("meow")
    i = i + 1
    # OR ->  i += 1

print("---------------------")

for j in [0, 1, 2]:
    print("meow")

print("---------------------")

print("meow\n" * 3, end="")

print("---------------------")

while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")

print("---------------------")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        a = int(input("What's a?"))
        if a > 0:
            break
    return a


def meow(a):
    for _ in range(a):
        print("meow")


main()
