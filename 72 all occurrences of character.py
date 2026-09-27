def all_occurrences(text, ch):
    for i in range(len(text)):
        if text[i] == ch:
            print(i)
text = input("Enter a string: ")
ch = input("Enter a character: ")
all_occurrences(text, ch)