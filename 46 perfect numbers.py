def perfect_numbers(n):
    for num in range(1, n + 1):
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total = total + i
        if total == num:
            print(num)
n = int(input("Enter a number: "))
perfect_numbers(n)