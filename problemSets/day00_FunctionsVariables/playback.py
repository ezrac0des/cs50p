def main():
    q = input("What needs to be slowed down? \n")
    pb(q)


def pb(q):
    print(q.strip().replace(" ", "..."))


main()
