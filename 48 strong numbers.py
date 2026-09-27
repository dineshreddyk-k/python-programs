def strong_numbers(n):
    for num in range(1, n + 1):
        temp = num
        total = 0
        while temp != 0:
            digit = temp % 10
            fact = 1
            for i in range(1, digit + 1):
                fact = fact * i
            total = total + fact
            temp = temp // 10
        if total == num:
            print(num)
n = int(input("Enter a number: "))
strong_numbers(n)