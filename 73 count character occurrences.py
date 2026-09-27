def count_occurrences(text, ch):
    count = 0
    for i in range(len(text)):
        if text[i] == ch:
            count = count + 1
    print("Occurrences =", count)
text = input("Enter a string: ")
ch = input("Enter a character: ")
count_occurrences(text, ch)