class calculator:
    __num1: str | float
    __num2: str | float
    ___operator: str
    __result: float

    def __init__(self) -> None:
        pass

    def calc(self):
        match self.___operator:
            case "+":
                return self.__num1 + self.__num2
            case "-":
                return self.__num1 - self.__num2
            case "*":
                return self.__num1 * self.__num2
            case "/":
                if self.__num2 == 0:
                    raise ZeroDivisionError("Não é possivel dividir por zero.")
                return self.__num1 / self.__num2
            case _:
                raise TypeError(f"Operador '{self.___operator}' inválido")

    def checkTypeNum(self, n: str) -> float:
        try:
            number = float(n)
            return number
        except ValueError:
            raise TypeError("Elemento digitado não é um número válido.")

    def make(self):
        n1 = input("Digite o primeiro número: ")
        self.__num1 = self.checkTypeNum(n1)

        n2 = input("Digite o segundo número: ")
        self.__num2 = self.checkTypeNum(n2)

        oper = input("Digite o operador matemático (+, -, *, /): ")
        self.___operator = oper

        self.__result = self.calc()

        print(f"Resultado: {self.__result}")
        return self.__result


calc = calculator()
calc.make()
