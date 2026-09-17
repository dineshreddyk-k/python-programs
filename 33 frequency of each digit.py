def frequency(n):
    count = [0] * 10
    while n != 0:
        digit = n % 10
        count[digit] = count[digit] + 1
        n = n // 10
    for i in range(10):
        if count[i] > 0:
            print(i, ":", count[i])
n = int(input("Enter a number: "))
frequency(n)