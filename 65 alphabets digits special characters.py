def count_characters(text):
    alphabet = 0
    digit = 0
    special = 0
    for ch in text:
        if ch.isalpha():
            alphabet = alphabet + 1
        elif ch.isdigit():
            digit = digit + 1
        else:
            special = special + 1
    print("Alphabets =", alphabet)
    print("Digits =", digit)
    print("Special characters =", special)
text = input("Enter a string: ")
count_characters(text)