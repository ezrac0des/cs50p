x = 1
y = 2
z = x + y
print(z)

a = int(input("What's a? \n"))
b = int(input("What's b? \n"))
print(a + b)

print(int(input("What's c? \n")) + int(input("What's d? \n")))

e = float(input("What's e? \n"))
f = float(input("What's f? \n"))
print(e + f)
# docs.python.org/3/library/functions.html#round
# round(number[, ndigits]) -> [] means optional in py
g = round(e + f)
print(f"{g:,}")

h = float(input("What's h? \n"))
i = float(input("What's i? \n"))
j = round(h / i, 2)
print(j)

k = float(input("What's k? \n"))
l = float(input("What's l? \n"))
m = k / l
print(f"{m:.2f}")
