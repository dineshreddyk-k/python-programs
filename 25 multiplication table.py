def multiplicationtable(n):
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i = i + 1
n = int(input("Enter a number: "))
multiplicationtable(n)