class table:
    # Variável de instância privada que armazena o número para
    # a tabela de multiplicação
    __number: int

    def __init__(self) -> None:
        # Método construtor que chama o método test_number()
        # ao instanciar a classe
        self.test_number()

    def multiplication_table(self):
        # Método para exibir a tabela de multiplicação do número
        print(f"Number {self.__number} multiplication table:")
        for i in range(1, 11):
            resultado = self.__number * i
            print(f"{self.__number} x {i} = {resultado}")

    def test_number(self):
        # Método para obter um número do usuário e exibir
        # a tabela de multiplicação
        try:
            self.__number = int(
                input("Enter a number to display the multiplication table: "))
            self.multiplication_table()
        except ValueError:
            # Captura um erro caso o usuário não insira um
            # número inteiro válido
            print("Error: Enter a valid integer.")


# Cria uma instância da classe table chamada tb, o que irá
# automaticamente chamar o construtor __init__()
tb = table()
