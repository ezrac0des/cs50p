try:
    x = int(input("What's x?"))
    print(f"x is {x}")  # VALUE ERROR
except ValueError:
    print("x is not an integer")

print("---------------------")

try:
    y = int(input("What's y?"))
except ValueError:
    print("y is not an integer")
else:
    print(f"y is {y}")  # NAME ERROR

print("---------------------")

while True:
    try:
        a = int(input("What's a?"))
    except ValueError:
        print("a is not an integer")
    else:
        print(f"a is {a}")
        break
# print(f"a is {a}")
print("---------------------")


def main():
    c = get_int()
    print(f"b is {c}")


def get_int():
    while True:
        try:
            # b = int(input("What's b?"))
            return int(input("What's b?"))
        except ValueError:
            pass
            # print("b is not an integer")
        # else:
            # print(f"b is {b}")
            # break
            # return b


main()

print("---------------------")

try:
    z = int(input("What's z?"))
except ValueError:
    print("z is not an integer")

print(f"z is {z}")  # NAME ERROR, of a non-integer value is entered!!
