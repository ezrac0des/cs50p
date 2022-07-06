def main():
    x = int(input("what's x? \n"))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)
    # return n ** 2
    # return n * n


main()
