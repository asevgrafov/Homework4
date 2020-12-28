from Utils import *
from Character import *
from Level import *
import random


class Game:
    spawner_to_factory_mapping = {"Warrior": WarriorFactory(),
                                  "Archer": ArcherFactory(),
                                  "Wizard": WizardFactory()}
    level_factory_mapping = {"Apple": AppleLevelFactory(),
                             "PickUp": PickUpLevelFactory(),
                             "Enemy": EnemyLevelFactory(),
                             "Totem": TotemLevelFactory()}
    hero_type_list = ["Warrior", "Archer", "Wizard"]
    level_types = ["Apple", "PickUp", "Enemy", "Totem"]

    def __init__(self) -> None:
        """
        Инициализируется начальное состояние игры с выбором персонажа
        """
        self.level_number = 1
        print("Выберите класс игрока")
        menu_items = []
        for i in range(len(self.hero_type_list)):
            print(str(i + 1) + ". " + str(self.hero_type_list[i]))
            menu_items.append(i + 1)
        a = get_int_input(menu_items)
        self.hero = self.spawner_to_factory_mapping[self.hero_type_list[a - 1]].create_character(Sword(10))
        self.hero.current_health = 100
        self.hero.max_health = 1000
        print("Вы выбрали персонажа:\n" + str(self.hero))

    def play(self) -> None:
        """
        Воспроизводит основную стадию игры, последовательно запускает
        каждый уровень и проверяет состояние между уровнями
        """
        while True:
            print()
            print("Уровень " + str(self.level_number))
            level = self.level_factory_mapping[random.choice(self.level_types)].create_level()
            if not level.play(self.hero, self.level_number):
                print("Game over!")
                break
            else:
                if self.hero.enemy_win_count == 4:
                    print("УРА! Вы победили!")
                    break
                else:
                    print(self.hero)
            input("Press Enter to continue...")
            self.level_number += 1


Game().play()
