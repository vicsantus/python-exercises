def vowels_counter(pattern_word: str):
    word = pattern_word.lower()
    vogais = "aeiou"
    if not word:
        return 0
    elif word[0] in vogais:
        return 1 + vowels_counter(word[1:])
    else:
        return vowels_counter(word[1:])


word = input("Enter a word: ")
count = vowels_counter(word)
print(f"The word '{word}' contains {count} vowels.")
