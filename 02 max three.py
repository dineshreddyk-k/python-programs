a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Max =", a)
elif b >= a and b >= c:
    print("Max =", b)
else:
    print("Max =", c)