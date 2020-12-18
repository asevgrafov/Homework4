from Character import *
import random

class InputValue():
    sol = ['apple', 'sword', 'enemy', 'bow', 'arrows', 'magic_book', 'totem']
    def get_int_input(self, values):
        while True:
            try:
                value = int(input())
                if value in values:
                    return value
                else:
                    print("Введенное значение некорректно. Введите значение заново!")
                    continue
            except ValueError:
                print("Введенное значение некорректно. Введите значение заново!")
                continue

    def random_choice(self):
        return random.choice(InputItems)

class InputCharacter(InputValue):

    def get_character(self, values):
        while True:
            print("Выберите своего персонажа: 1 - Воин, 2 - Лучник, 3 - Маг")
            a = a.get_int_input(self, [1, 2, 3])
            if not 1 <= a <= 3:
                print("Введенное число не находится в диапазоне возможных значений")
                return 0
            if a == 1:
                print("Вы выбрали воина")
                return Warrior()
            if a == 2:
                print("Вы выбрали лучника")
                return Archer()
            if a == 3:
                print("Вы выбрали мага")
                return Wizard()

class InputItems(InputValue):

    def take_item(self):
        pass

    def take_apple(self):
        print("Take apple")

    def take_totem(self):
        print("Take totem")

    def take_sword(self):
        print("Take sword")

    def take_bow(self):
        print("take bow")

    def take_arrows(self):
        print("Take arrows")

    def take_magic_book(self):
        print("Take magic_book")




#
# class InputSword(InputValue):
#
#     def input_sword(self):
#         while True:
#             print("1 - Взять меч" + " " + "2 - Пройти мимо меча")
#             a = get_int_input([1, 2])
#             if not 1 <= a <= 2:
#                 print("Введенное число не находится в диапазоне возможных значений")
#                 return 0
#             if a == 1:
#                 knight['strenght'] = sword
#                 return knight['strenght']
#             if a == 2:
#                 break
#
#
#
#
# class TakeApple(InputValue):
#
#     def take_apple():
#         knight['health'] += apple
#         print("Вы нашли яблочко! Ваше количество жизней =" + ' ' + str(knight['health']) + "\n")
#
# class TakeSword(InputValue):
#
#     def take_mech():
#         print("Сила меча =" + " " + str(sword))
#         input_sword()
#         print("Сила рыцаря равна" + " " + str(knight['strenght']) + "\n")
#
#
#     def random_ch(sol):
#         count = 0
#         while True:
#             if knight['health'] <= 0:
#                 print("Игра окончена!")
#                 break
#             if random.choice(sol) == "apple":
#                 take_apple()
#             if random.choice(sol) == 'mech':
#                 take_mech()
#             if random.choice(sol) == "enemy":
#                 print("Вы встретили чудовище c " + str(enemy['health']) + " жизнями и с силой удара " + str(
#                     enemy['strenght']))
#                 count += fight(count)
#             if count >= 10:
#                 print("Вы победили! УРА!")
#                 break





