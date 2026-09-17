def numberwords(n):
    words = ["Zero", "One", "Two", "Three", "Four",
             "Five", "Six", "Seven", "Eight", "Nine"]
    if n == 0:
        print("Zero")
        return
    reverse = 0
    while n != 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    while reverse != 0:
        digit = reverse % 10
        print(words[digit], end=" ")
        reverse = reverse // 10
n = int(input("Enter a number: "))
numberwords(n)