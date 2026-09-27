def count_vowels_consonants(text):
    vowels = 0
    consonants = 0
    for ch in text:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonants = consonants + 1
    print("Vowels =", vowels)
    print("Consonants =", consonants)
text = input("Enter a string: ")
count_vowels_consonants(text)