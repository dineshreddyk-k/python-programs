def sumfirstlast(n):
    last = n % 10
    while n >= 10:
        n = n // 10
    first = n
    total = first + last
    print("First digit =", first)
    print("Last digit =", last)
    print("Sum =", total)
n = int(input("Enter a number: "))
sumfirstlast(n)