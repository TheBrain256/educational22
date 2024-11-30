class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor +1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break




h1 = House('ЖК Лучшая жизнь', 25)
h2 = House('Хрущёвка', 5)
h1.go_to(4)
h2.go_to(0)
