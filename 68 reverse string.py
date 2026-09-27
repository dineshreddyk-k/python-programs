def reverse_string(text):
    reverse = ""
    for i in range(len(text) - 1, -1, -1):
        reverse = reverse + text[i]
    print("Reverse =", reverse)
text = input("Enter a string: ")
reverse_string(text)