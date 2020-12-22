from abc import ABC, abstractmethod
from typing import Dict


class Items(ABC):
    def __init__(self) -> None:
        self.name = ""

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class Equipment(Items):
    def __init__(self) -> None:
        super(Equipment, self).__init__()
        self.damage = 0

    def get_damage(self) -> int:
        return self.damage

    def __str__(self) -> str:
        return self.name + " урон: " + str(self.damage)


class Sword(Equipment):
    def __init__(self, d: int) -> None:
        super(Sword, self).__init__()
        self.damage = d
        self.name = "Меч"


class Bow(Equipment):

    def __init__(self, d: int) -> None:
        super(Bow, self).__init__()
        self.damage = d
        self.name = "Лук"


class Arrows(Equipment):

    def __init__(self, d: int) -> None:
        super(Arrows, self).__init__()
        self.damage = d
        self.name = "Стрелы"


class MagicBook(Equipment):

    def __init__(self, d: int) -> None:
        super(MagicBook, self).__init__()
        self.damage = d
        self.name = "Магическая книга"


class Apple(Items):
    def __init__(self) -> None:
        super(Apple, self).__init__()
        self.name = "Яблоко"
        self.heal = 0


class Totem(Items):
    def __init__(self) -> None:
        super(Totem, self).__init__()
        self.name = "Тотем"
        self.current_health: int = None
        self.items: Dict[str, Equipment] = None
        self.enemy_win_count: int = None