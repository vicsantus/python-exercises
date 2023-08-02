def palindrome(word):
    # Função para verificar se uma palavra é um palíndromo
    # A palavra é comparada com sua versão invertida (usando a sintaxe [::-1])
    if word == word[::-1]:
        print(f"The word {word} is a palindrome.")
        return f"The word {word} is a palindrome."

    # Se a palavra não é igual à sua versão invertida, não é um palíndromo
    print(f"The word {word} is not a palindrome.")
    return f"The word {word} is not a palindrome."


if __name__ == "__main__":
    # Teste da função: verifica se a palavra 'maman' é um palíndromo
    palindrome(input("Enter the word: ").lower())
