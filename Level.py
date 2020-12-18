from abc import ABC, abstractmethod
from Items import *
import random
from Utils import *


class Level(ABC):

    @abstractmethod
    def play(self, hero, n) -> bool:
        pass

class AppleLevel(Level):

    def play(self, hero, n) -> bool:
        apple = Apple()
        apple.heal = random.randrange(3, 10)
        if hero.current_health + apple.heal > hero.max_health:
            hero.current_health = hero.max_health
        else:
            hero.current_health += apple.heal
        print("Герой съел яблоко и вылечился на " + str(apple.heal) + " здоровья")
        return True

class PickUpLevel(Level):
    equipment_types = ["Sword", "Bow", "Arrows", "Magic_book"]
    def play(self, hero, n) -> bool:
        equipment_type = random.choice(self.equipment_types)
        equipment = None
        if equipment_type == "Sword":
            equipment = Sword(random.randrange(3,20))
        if equipment_type == "Bow":
            equipment = Bow(random.randrange(3,20))
        if equipment_type == "Arrows":
            equipment = Arrows(random.randrange(3,20))
        if equipment_type == "Magic_book":
            equipment = MagicBook(random.randrange(3,20))
        print("Вы нашли предмет: ")
        print(equipment)
        print("1 - Подобрать предмет, 2 - Пройти мимо")
        a = get_int_input([1,2])
        if a == 1:
            hero.take_weapon(equipment)
            print("Вы подобрали предмет " + str(equipment))
        return True


class LevelFactory(ABC):

    @abstractmethod
    def create_level(self):
        pass

class AppleLevelFactory(LevelFactory):
    def create_level(self):
        return AppleLevel()

class PickUpLevelFactory(LevelFactory):
    def create_level(self):
        return PickUpLevel()

