def final_value(initial_cap, fees, time_in_mounths):
    # Calcula o valor final do investimento com base
    # no capital inicial, taxas de juros e tempo em meses
    decimal_fees_tax = fees / 100
    final_value = initial_cap * (1 + decimal_fees_tax) ** time_in_mounths
    return final_value


def make_investiment():
    # Função para interagir com o usuário e calcular
    # o valor final do investimento
    try:
        # Solicita ao usuário que insira o capital
        # inicial, as taxas de juros e o tempo em meses
        initial_cap = float(input("Enter the starting capital: $"))
        fees = float(input("Enter the interest rate (%): "))
        time_in_mounths = int(input("Enter investment time in months: "))

        # Calcula o valor final do investimento usando a função final_value()
        value = final_value(initial_cap, fees, time_in_mounths)

        # Exibe o valor final do investimento na tela com 2 casas decimais
        print(f"The final investment amount will be: ${value:.2f}")
    except ValueError:
        # Captura um erro caso o usuário não insira valores numéricos válidos
        print("Error: Please enter valid numerical values.")


if __name__ == "__main__":
    # Chama a função make_investiment() ao executar o programa
    make_investiment()
