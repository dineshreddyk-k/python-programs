def sumodd(n):
    i = 1
    total = 0
    while i <= n:
        if i % 2 != 0:
            total = total + i
        i = i + 1
    print("Sum of odd numbers =", total)
n = int(input("Enter n: "))
sumodd(n)