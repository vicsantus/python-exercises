class calculator:
    # Variáveis de instância privadas que armazenam os números,
    # o operador e o resultado da operação
    __num1: str | float
    __num2: str | float
    ___operator: str
    __result: float

    def __init__(self) -> None:
        self.make()

    def calc(self):
        # Método para realizar a operação matemática com base no
        # operador fornecido pelo usuário
        match self.___operator:
            case "+":
                return self.__num1 + self.__num2
            case "-":
                return self.__num1 - self.__num2
            case "*":
                return self.__num1 * self.__num2
            case "/":
                # Verifica se o divisor é zero e lança um erro caso seja
                if self.__num2 == 0:
                    raise ZeroDivisionError(
                        "It is not possible to divide by zero.")
                return self.__num1 / self.__num2
            case _:
                # Lança um erro caso o operador seja inválido
                raise TypeError(f"Invalid '{self.___operator}' operator")

    def checkTypeNum(self, n: str) -> float:
        # Método para verificar se uma string pode ser convertida
        # em um número (float)
        try:
            number = float(n)
            return number
        except ValueError:
            # Lança um erro caso a conversão não seja possível
            raise TypeError("Element entered is not a valid number.")

    def make(self):
        # Método principal para obter os números e operador
        # do usuário e realizar a operação
        n1 = input("Enter the first number: ")
        self.__num1 = self.checkTypeNum(n1)

        n2 = input("Enter the second number: ")
        self.__num2 = self.checkTypeNum(n2)

        oper = input("Enter the math operator (+, -, *, /): ")
        self.___operator = oper

        self.__result = self.calc()

        # Exibe o resultado da operação na tela e retorna o valor do resultado
        print(f"Result: {self.__result}")
        return self.__result


# Cria uma instância da classe calculator e chama o método
calc = calculator()
