def last_occurrence(text, ch):
    position = -1
    for i in range(len(text)):
        if text[i] == ch:
            position = i
    if position != -1:
        print("Last occurrence =", position)
    else:
        print("Character not found")
text = input("Enter a string: ")
ch = input("Enter a character: ")
last_occurrence(text, ch)