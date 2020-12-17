from abc import ABC, abstractmethod
from Items import *

class Character(ABC):
    current_health = 100
    max_health = 100
    items = {"sword": None, "magic_book": None, "bow": None, "arrows": None}
    totem = None

    def attack(self, type_weapon):
        arrow_damage = 0
        if type_weapon == "bow":
            arrow_damage = self.items['arrows'].get_damage()
        return self.items[type_weapon].get_damage()+arrow_damage

    def take_weapon(self, weapon):
        if isinstance(weapon, Sword):
            self.items['sword'] = weapon
        if isinstance(weapon, Bow):
            self.items['bow'] = weapon
        if isinstance(weapon, Arrows):
            self.items['arrows'] = weapon
        if isinstance(weapon, MagicBook):
            self.items['magic_book'] = weapon


class Wizard(Character):
    def attack(self, type_weapon):
        attack_k = 1
        if type_weapon == "magic_book":
            attack_k *= 1.1
        return self.attack(type_weapon)*attack_k


class Archer(Character):
    def attack(self, type_weapon):
        attack_k = 1
        if type_weapon == "magic_book":
            attack_k *= 1.1
        return self.attack(type_weapon)*attack_k


class Warrior(Character):
    def attack(self, type_weapon):
        attack_k = 1
        if type_weapon == "magic_book":
            attack_k *= 1.1
        return self.attack(type_weapon)*attack_k


class CharacterFactory(ABC):

    @abstractmethod
    def create_character(self, weapon=None):
        pass


class WizardFactory(CharacterFactory):
    def create_character(self, weapon=None):
        wizard = Wizard()
        if weapon == None:
            wizard.take_weapon(MagicBook(10))
        else:
            wizard.take_weapon(weapon)
        return wizard



class ArcherFactory(CharacterFactory):
    def create_character(self, weapon=None):
        archer = Archer()
        if weapon == None:
            archer.take_weapon(Bow(10))
            archer.take_weapon(Arrows(10))
        else:
            archer.take_weapon(weapon)
        return archer


class WarriorFactory(CharacterFactory):
    def create_character(self, weapon=None):
        warrior = Warrior()
        if weapon == None:
            warrior.take_weapon(Sword(10))
        else:
            warrior.take_weapon(weapon)
        return warrior