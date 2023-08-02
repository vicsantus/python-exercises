class average():
    # Variável de classe que armazena as notas dos cursos
    __grades = []

    def __init__(self) -> None:
        # Método construtor que chama o método ask_for_grades()
        # ao instanciar a classe
        self.ask_for_grades()

    def calc_average(self):
        # Método para calcular a média das notas dos cursos
        media = sum(self.__grades) / len(self.__grades)
        return media

    def ask_for_grades(self):
        # Método para solicitar ao usuário que digite as notas dos cursos
        for i in range(3):
            nota = float(input(f"Enter grade for course {i + 1}: "))
            self.__grades.append(nota)

        # Calcula a média das notas e exibe o resultado na tela
        media = self.calc_average()
        print(f"The average grade is: {media:.2f}")
        return f"The average grade is: {media:.2f}"


# Cria uma instância da classe average chamada makeAvg,
# o que irá automaticamente chamar o construtor __init__()
makeAvg = average()
