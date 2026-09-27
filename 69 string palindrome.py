def palindrome(text):
    reverse = ""
    for i in range(len(text) - 1, -1, -1):
        reverse = reverse + text[i]
    if text == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")
text = input("Enter a string: ")
palindrome(text)