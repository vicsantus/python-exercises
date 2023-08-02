import random


# Função para verificar se um número é primo usando
# o Teste de Primalidade de Fermat.
# Recebe o número n como entrada e um parâmetro opcional k (número de testes).
# Retorna True se o número for provavelmente primo e False caso contrário.
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Função interna para verificar se a testemunha "a" é um
    # provável divisor de "n".
    # Utiliza o pequeno teorema de Fermat.
    def check_witness(a, n):
        x = pow(a, n - 1, n)  # Calcula (a^(n-1)) % n de forma eficiente.
        return x == 1

    # Realiza k iterações do teste de Fermat para maior confiabilidade.
    for _ in range(k):
        # Escolhe um número aleatório entre 2 e n-2.
        a = random.randint(2, n - 2)
        if not check_witness(a, n):
            return False

    return True


# Função para gerar os primeiros "n" números primos.
# Recebe o parâmetro opcional "n" que define a quantidade de
# números primos a gerar (padrão é 10).
# Retorna uma lista com os primeiros "n" números primos.
def ten_primes(n=10):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


if __name__ == "__main__":
    print(ten_primes())
