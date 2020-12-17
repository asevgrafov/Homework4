from abc import ABC, abstractmethod

class Items(ABC):
    name = ""
    def get_name(self):
        return self.name


class Equipment(Items):
    damage = 0

    def get_damage(self):
        return self.damage


class Sword(Equipment):
    name = "Меч"

    def __init__(self, d):
        self.damage = d


class Bow(Equipment):
    name = "Лук"

    def __init__(self, d):
        self.damage = d


class Arrows(Equipment):
    name = "Стрелы"

    def __init__(self, d):
        self.damage = d


class MagicBook(Equipment):
    name = "Магическая книга"

    def __init__(self, d):
        self.damage = d


class Apple(Items):
    name = "Яблоко"
    heal = 0

class Totem(Items):
    name = "Тотем"
    state = 0