def factors(n):
    i = 1
    while i <= n:
        if n % i == 0:
            print(i)
        i = i + 1
n = int(input("Enter a number: "))
factors(n)