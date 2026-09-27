def check_numbers(numbers):
    print("Even numbers:")
    for n in numbers:
        if n % 2 == 0:
            print(n)
    print("Odd numbers:")
    for n in numbers:
        if n % 2 != 0:
            print(n)
    print("Prime numbers:")
    for n in numbers:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            print(n)
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)
check_numbers(numbers)