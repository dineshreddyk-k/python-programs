def armstrong_numbers(n):
    for num in range(1, n + 1):
        temp = num
        total = 0
        while temp != 0:
            digit = temp % 10
            total = total + digit * digit * digit
            temp = temp // 10
        if num == total:
            print(num)
n = int(input("Enter a number: "))
armstrong_numbers(n)