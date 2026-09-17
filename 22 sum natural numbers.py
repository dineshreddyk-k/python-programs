def sumnumbers(n):
    i = 1
    total = 0
    while i <= n:
        total = total + i
        i = i + 1
    print("Sum =", total)
n = int(input("Enter n: "))
sumnumbers(n)