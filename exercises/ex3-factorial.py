def factorial(n):
    # Função para calcular o fatorial de um número
    # Caso base: Se n for menor ou igual a 0, o fatorial é 1
    if n <= 0:
        return 1

    # Chamada recursiva: retorna n multiplicado pelo fatorial de (n - 1)
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Teste da função: calcula o fatorial de 10 e imprime o resultado
    print(factorial(int(input("Enter the number you want to factorial: "))))
