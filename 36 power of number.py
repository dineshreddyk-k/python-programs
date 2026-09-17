def power(n, p):
    result = 1
    for i in range(p):
        result = result * n
    print("Power =", result)
n = int(input("Enter a number: "))
p = int(input("Enter power: "))
power(n, p)