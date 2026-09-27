def first_occurrence(text, ch):
    for i in range(len(text)):
        if text[i] == ch:
            print("First occurrence =", i)
            return
    print("Character not found")
text = input("Enter a string: ")
ch = input("Enter a character: ")
first_occurrence(text, ch)