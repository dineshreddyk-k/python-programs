def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total = total + i
    if total == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
n = int(input("Enter a number: "))
perfect(n)