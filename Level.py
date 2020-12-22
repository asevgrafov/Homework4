from abc import ABC, abstractmethod
from Items import *
import random
from Utils import *
from Character import *


class Level(ABC):

    @abstractmethod
    def play(self, hero: Character, n: int) -> bool:
        """
        Происходит проигрывание конкретного уровня
        """
        pass


class AppleLevel(Level):
    """
    Класс уровня на котором герой съедает яблоко
    """

    def play(self, hero: Character, n: int) -> bool:
        apple = Apple()
        apple.heal = random.randrange(3, 10)
        if hero.current_health + apple.heal > hero.max_health:
            hero.current_health = hero.max_health
        else:
            hero.current_health += apple.heal
        print("Герой съел яблоко и вылечился на " + str(apple.heal) + " здоровья")
        return True


class PickUpLevel(Level):
    """
    Класс уровня на котором герой может поднять предмет
    """
    equipment_types = ["Sword", "Bow", "Arrows", "Magic_book"]

    def play(self, hero: Character, n: int) -> bool:
        equipment_type = random.choice(self.equipment_types)
        equipment: Equipment = None
        if equipment_type == "Sword":
            equipment = Sword(random.randrange(3, 20))
        if equipment_type == "Bow":
            equipment = Bow(random.randrange(3, 20))
        if equipment_type == "Arrows":
            equipment = Arrows(random.randrange(3, 20))
        if equipment_type == "Magic_book":
            equipment = MagicBook(random.randrange(3, 20))
        print("Вы нашли предмет: ")
        print(equipment)
        print("1 - Подобрать предмет, 2 - Пройти мимо")
        a = get_int_input([1, 2])
        if a == 1:
            hero.take_weapon(equipment)
            print("Вы подобрали предмет " + str(equipment))
        return True


class EnemyLevel(Level):
    """
    Класс уровня на котором герой встречается с врагом
    """
    spawner_to_factory_mapping = {"Warrior": WarriorFactory(), "Archer": ArcherFactory(), "Wizard": WizardFactory()}
    enemy_types = ["Warrior", "Archer", "Wizard"]

    def play(self, hero: Character, n: int) -> bool:
        enemy_type = random.choice(self.enemy_types)
        enemy = self.spawner_to_factory_mapping[enemy_type].create_character()
        print("Вы встретили врага: \n" + str(enemy))
        if not self.is_fighting():
            return True
        # Текущий ход героя
        hero_step = True
        while hero.current_health > 0 and enemy.current_health > 0:
            self.step(hero, enemy, hero_step)
            hero_step = not hero_step
        if hero.current_health > 0:
            hero.enemy_win_count += 1
            return True
        elif hero.totem is not None:
            hero.restore_from_totem()
            print("\nПоказатели героя были восстановлены\n")
            return True
        else:
            return False

    def step(self, hero: Character, enemy: Character, hero_step: int) -> None:
        """
        Шаг боя
        """
        if hero_step:
            enemy.current_health -= int(hero.attack(self.pick_available_weapon(hero)))
            print("Здоровье врага после удара героя " + str(enemy.current_health))
        else:
            hero.current_health -= int(enemy.attack() * self.get_defence(hero, enemy))
            print("Здоровье героя после удара врага " + str(hero.current_health))

    def pick_available_weapon(self, hero: Character) -> str:
        """
        Выбор доступного оружия для атаки
        """
        print("Каким оружием вы хотите атаковать врага?")
        weapons = hero.get_available_weapons()
        menu_items = []
        for i in range(0, len(weapons)):
            menu_items.append(i + 1)
            print(str(i + 1) + " " + str(weapons[i]))
        a = get_int_input(menu_items)
        select_weapon = weapons[a - 1]
        if isinstance(select_weapon, Sword):
            return "Sword"
        if isinstance(select_weapon, Bow):
            return "Bow"
        if isinstance(select_weapon, MagicBook):
            return "Magic_book"
        else:
            return ""

    def get_defence(self, hero: Character, enemy: Character) -> float:
        """
        Порезка урона, если класс героя совпадает с классом врага
        """
        if type(hero) == type(enemy):
            return 0.5
        else:
            return 1

    def is_fighting(self) -> bool:
        """
        Выбор героя: сразиться или убежать
        """
        print("1 - Сразиться, 2 - Убежать")
        a = get_int_input([1, 2])
        if a == 1:
            return True
        else:
            return False


class TotemLevel(Level):
    """
    Класс уровня на котором герой может поднять тотем
    """
    def play(self, hero: Character, n: int) -> bool:
        print("Вы нашли тотем: ")
        print("1 - Подобрать, 2 - Пройти мимо")
        a = get_int_input([1, 2])
        if a == 1:
            hero.save_to_totem()
        return True


class LevelFactory(ABC):

    @abstractmethod
    def create_level(self) -> Level:
        """
        Создание уровня
        """
        pass


class AppleLevelFactory(LevelFactory):
    """
    Класс создания уровня "яблоко"
    """
    def create_level(self) -> AppleLevel:
        return AppleLevel()


class PickUpLevelFactory(LevelFactory):
    """
    Класс создания уровня "поднятие предмета"
    """
    def create_level(self) -> PickUpLevel:
        return PickUpLevel()


class EnemyLevelFactory(LevelFactory):
    """
    Класс создания уровня "встреча с врагом"
    """
    def create_level(self) -> EnemyLevel:
        return EnemyLevel()


class TotemLevelFactory(LevelFactory):
    """
    Класс создания уровня "тотем"
    """
    def create_level(self) -> TotemLevel:
        return TotemLevel()
