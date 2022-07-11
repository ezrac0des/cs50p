def main():
    q = input("What is your command? \n")
    command(q)


def command(q):
    print(q.strip().lower())


main()
