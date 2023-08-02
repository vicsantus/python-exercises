def vowels_counter(pattern_word: str):
    # Converte a palavra para minúsculas para não
    # diferenciar entre maiúsculas e minúsculas
    word = pattern_word.lower()

    # Define as vogais que serão contadas
    vogais = "aeiou"

    # Verifica se a palavra é vazia. Se for, não há vogais e retorna 0.
    if not word:
        return 0

    # Verifica se a primeira letra da palavra é uma vogal.
    # Se for, conta 1 e chama recursivamente a
    # função para o restante da palavra.
    elif word[0] in vogais:
        return 1 + vowels_counter(word[1:])

    # Se a primeira letra não for uma vogal,
    # chama recursivamente a função para o restante da palavra.
    else:
        return vowels_counter(word[1:])


word = input("Enter a word: ")
count = vowels_counter(word)
print(f"The word '{word}' contains {count} vowels.")
