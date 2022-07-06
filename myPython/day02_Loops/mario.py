print("#")
print("#")
print("#")

print("---------------------")

for _ in range(3):
    print("#")

print("---------------------")


def main():
    print_column(3)
    print("---------------------")
    print_row(4)
    print("---------------------")
    print_square(3)


def print_column(height):
    for _ in range(3):
        print("#")
    # OR  ->   print("#\n" * height, end="")


def print_row(width):
    print("?" * width)


def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # bricks
            print("#", end="")
        print()


main()

print("---------------------")
