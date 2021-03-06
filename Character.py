from abc import ABC, abstractmethod
from Items import *
from typing import Dict


class Character(ABC):
    """
    Класс персонажа
    """
    def __init__(self) -> None:
        self.current_health = 80
        self.max_health = 100
        self.items: Dict[str, Equipment] = {"Sword": None, "Magic_book": None, "Bow": None, "Arrows": None}
        self.totem: Totem = None
        self.enemy_win_count = 0

    def attack(self, type_weapon: str = None) -> float:
        """
        Вычисление количества нанесенного урона
        """
        arrow_damage = 0
        if type_weapon == "Bow":
            arrow_damage = self.items['Arrows'].get_damage()
        return self.items[type_weapon].get_damage() + arrow_damage

    def take_weapon(self, weapon: Equipment) -> None:
        """
        Добавления оружия в инвентарь
        """
        if isinstance(weapon, Sword):
            self.items['Sword'] = weapon
        if isinstance(weapon, Bow):
            self.items['Bow'] = weapon
        if isinstance(weapon, Arrows):
            self.items['Arrows'] = weapon
        if isinstance(weapon, MagicBook):
            self.items['Magic_book'] = weapon

    def get_inventory_string(self) -> str:
        """
        Отображение содержимого инвенторя
        """
        stroka = "В инвентаре есть:\n"
        for k, item in self.items.items():
            if item is not None:
                stroka += str(item) + "\n"
        if self.totem is not None:
            stroka += str(self.totem) + "\n"
        return stroka

    def __str__(self) -> str:
        return "Здоровье персонажа " + str(self.current_health) + " из " \
               + str(self.max_health) + "\n" + "Побеждено врагов: " \
               + str(self.enemy_win_count) + "\n" + self.get_inventory_string()

    def get_available_weapons(self) -> list:
        """
        Выбор доступного оружия
        """
        weapons = [] # type: list
        if self.items["Sword"] is not None:
            weapons.append(self.items["Sword"])
        if self.items["Magic_book"] is not None:
            weapons.append(self.items["Magic_book"])
        if self.items["Bow"] is not None and self.items["Arrows"] is not None:
            weapons.append(self.items["Bow"])
        return weapons

    def save_to_totem(self) -> None:
        """
        Сохранение параметров героя при поднятии тотема
        """
        totem = Totem()
        totem.current_health = self.current_health
        totem.items = self.items.copy()
        totem.enemy_win_count = self.enemy_win_count
        self.totem = totem

    def restore_from_totem(self) -> None:
        """
        Восстановление параметров героя из тотема
        """
        self.current_health = self.totem.current_health
        self.items = self.totem.items
        self.enemy_win_count = self.totem.enemy_win_count
        self.totem = None


class Wizard(Character):
    """
    Персонаж класса маг
    """
    def attack(self, type_weapon: str = "Magic_book") -> float:
        attack_k: float = 1
        if type_weapon == "Magic_book":
            attack_k *= 1.1
        return super(Wizard, self).attack(type_weapon) * attack_k

    def __str__(self) -> str:
        return "класс волшебник\n" + str(super(Wizard, self).__str__())


class Archer(Character):
    """
    Персонаж класса лучник
    """
    def attack(self, type_weapon: str = "Bow") -> float:
        attack_k: float = 1
        if type_weapon == "Bow":
            attack_k *= 1.1
        return super(Archer, self).attack(type_weapon) * attack_k

    def __str__(self) -> str:
        return "класс лучник\n" + str(super(Archer, self).__str__())


class Warrior(Character):
    """
    Персонаж класса воин
    """
    def attack(self, type_weapon: str = "Sword") -> float:
        attack_k: float = 1
        if type_weapon == "Sword":
            attack_k *= 1.1
        return super(Warrior, self).attack(type_weapon) * attack_k

    def __str__(self) -> str:
        return "класс воин\n" + str(super(Warrior, self).__str__())


class CharacterFactory(ABC):

    @abstractmethod
    def create_character(self, weapon: Equipment = None) -> Character:
        pass


class WizardFactory(CharacterFactory):

    def create_character(self, weapon: Equipment = None) -> Wizard:
        """
        Класс создания персонажа маг
        """
        wizard = Wizard()
        if weapon is None:
            wizard.take_weapon(MagicBook(10))
        else:
            wizard.take_weapon(weapon)
        return wizard


class ArcherFactory(CharacterFactory):
    """
    Класс создания персонажа лучник
    """
    def create_character(self, weapon: Equipment = None) -> Archer:
        archer = Archer()
        if weapon is None:
            archer.take_weapon(Bow(10))
            archer.take_weapon(Arrows(10))
        else:
            archer.take_weapon(weapon)
        return archer


class WarriorFactory(CharacterFactory):
    """
    Класс создания персонажа воин
    """
    def create_character(self, weapon: Equipment = None) -> Warrior:
        warrior = Warrior()
        if weapon is None:
            warrior.take_weapon(Sword(10))
        else:
            warrior.take_weapon(weapon)
        return warrior
