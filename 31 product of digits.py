def productdigits(n):
    product = 1
    while n != 0:
        digit = n % 10
        product = product * digit
        n = n // 10
    print("Product of digits =", product)
n = int(input("Enter a number: "))
productdigits(n)