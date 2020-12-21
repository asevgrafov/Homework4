from abc import ABC, abstractmethod

class Items(ABC):
    def __init__(self):
        self.name = ""

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

class Equipment(Items):
    def __init__(self):
        super(Equipment, self).__init__()
        self.damage = 0

    def get_damage(self):
        return self.damage

    def __str__(self):
        return self.name + " урон: " + str(self.damage)

class Sword(Equipment):

    def __init__(self, d):
        super(Sword, self).__init__()
        self.damage = d
        self.name = "Меч"

class Bow(Equipment):


    def __init__(self, d):
        super(Bow, self).__init__()
        self.damage = d
        self.name = "Лук"

class Arrows(Equipment):


    def __init__(self, d):
        super(Arrows, self).__init__()
        self.damage = d
        self.name = "Стрелы"

class MagicBook(Equipment):


    def __init__(self, d):
        super(MagicBook, self).__init__()
        self.damage = d
        self.name = "Магическая книга"

class Apple(Items):
    def __init__(self):
        super(Apple, self).__init__()
        self.name = "Яблоко"
        self.heal = 0

class Totem(Items):
    def __init__(self):
        super(Totem, self).__init__()
        self.name = "Тотем"
        self.current_health = None
        self.items = None
        self.enemy_win_count = None