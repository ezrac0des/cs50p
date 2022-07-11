# ask user for their name FIRST PYTHON!!!

print("hello world")
print("first python try")
print(5 + 6)

"""
ANYTHING IN BETWEEN THREE DOUBLE QUOTES ARE COMMENTS (MULTI COMMENT LINE)
"""
# removes whitespace from and capitalizes first letter of each word
name = input("What's your name? \n").strip().title()

# removes whitespace from str
name = name.strip()

# capitalizes user's name
name = name.capitalize()

# capitalizes all word's first letter
name = name.title()

print("FIRST WAY:")
print("hello, " + name)
print(" ")

print("SECOND WAY:")
print("hello,", name)
print(" ")

print("THIRD WAY:")
print("hello, ")
print(name)
print(" ")

print("FOURTH WAY:")
print("hello,", end=" ")
print(name)
print(" ")

print("FIFTH WAY:")
print("hello,", name, sep=" ")
print(" ")

print("SIXTH WAY:")
print("hello, \"friend\"")
print(" ")

print("SEVENTH WAY:")
print(f"hello, {name}")

# docs.python.org
# docs.python.org/3/library/functions.html
# docs.python.org/3/library/functions.html#print
# docs.python.org/3/library/stdtypes.html#string-methods
