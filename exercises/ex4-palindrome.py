def palindrome(word):
    if word == word[::-1]:
        print("The word is a palindrome.")
        return "The word is a palindrome."

    print("The word is not a palindrome.")
    return "The word is not a palindrome."


if __name__ == "__main__":
    palindrome('maman')
