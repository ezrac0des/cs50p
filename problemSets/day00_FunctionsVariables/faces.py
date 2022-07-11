def main():
    f = input("ready to make some faces? \n")
    convert(f)


def convert(f):
    print(f.replace(":)", "🙂").replace(":(", "🙁"))



main()