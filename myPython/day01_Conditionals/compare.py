x = int(input("What's x? "))
y = int(input("What's y? "))

# first way (introduced to if statement)
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# second way (introduced to elif & else statement)
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# third way (introduced to or)
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# fourth way (introduced to ==)
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# fourth way (introduced to !=)
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
