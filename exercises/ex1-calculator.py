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
                    raise ZeroDivisionError(
                        "It is not possible to divide by zero.")
                return self.__num1 / self.__num2
            case _:
                raise TypeError(f"Invalid '{self.___operator}' operator")

    def checkTypeNum(self, n: str) -> float:
        try:
            number = float(n)
            return number
        except ValueError:
            raise TypeError("Element entered is not a valid number.")

    def make(self):
        n1 = input("Enter the first number: ")
        self.__num1 = self.checkTypeNum(n1)

        n2 = input("Enter the second number: ")
        self.__num2 = self.checkTypeNum(n2)

        oper = input("Enter the math operator (+, -, *, /): ")
        self.___operator = oper

        self.__result = self.calc()

        print(f"Result: {self.__result}")
        return self.__result


calc = calculator()
calc.make()
