class table:
    __number: int

    def __init__(self) -> None:
        pass

    def multiplication_table(self):
        print(f"Number {self.__number} multiplication table:")
        for i in range(1, 11):
            resultado = self.__number * i
            print(f"{self.__number} x {i} = {resultado}")

    def test_number(self):
        try:
            self.__number = int(
                input("Enter a number to display the multiplication table: "))
            self.multiplication_table()
        except ValueError:
            print("Error: Enter a valid integer.")


tb = table()
tb.test_number()
