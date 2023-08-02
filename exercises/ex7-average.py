class average():
    __grades = []

    def __init__(self) -> None:
        self.ask_for_grades()

    def calc_average(self):
        media = sum(self.__grades) / len(self.__grades)
        return media

    def ask_for_grades(self):
        for i in range(3):
            nota = float(input(f"Enter grade for course {i + 1}: "))
            self.__grades.append(nota)

        media = self.calc_average()
        print(f"The average grade is: {media:.2f}")
        return f"The average grade is: {media:.2f}"


makeAvg = average()
