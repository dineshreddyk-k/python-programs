def prime_sum(n):
    total = 0
    for num in range(2, n + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        if count == 2:
            total = total + num
    print("Sum of prime numbers =", total)
n = int(input("Enter a number: "))
prime_sum(n)