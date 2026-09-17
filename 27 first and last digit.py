def firstlast(n):
    last = n % 10
    while n >= 10:
        n = n // 10
    first = n
    print("First digit =", first)
    print("Last digit =", last)
n = int(input("Enter a number: "))
firstlast(n)