def armstrong(n):
    temp = n
    total = 0
    while n != 0:
        digit = n % 10
        total = total + digit * digit * digit
        n = n // 10
    if temp == total:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
n = int(input("Enter a number: "))
armstrong(n)