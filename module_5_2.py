# Специальные методы классов
# Задача "Магические здания"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to_(self, new_floor):
        if type(new_floor) != int or new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return "Название: " + self.name + ", кол-во этажей: " + str(self.number_of_floors)


House_1 = House('ЖК Эльбрус', 30)
House_2 = House('ЖК Лесное', 5)
House_3 = House('Реконструкция', 3)

# __str__
print(House_1)
print(House_2)
print(House_3)

# __len__
print(len(House_1))
print(len(House_2))
print(len(House_3))
