import random
#Ghjcnj rjvvtynfhbq

sol = ['apple', 'enemy', 'mech']
knight = {'health': 10, 'strenght': 10}
enemy = {'health': 2, 'strenght': 2}
current_enemy = {'health': 0, 'strenght': 0}
apple = 0
sword = 1


def get_int_input(values):
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


def input_sword():
    while True:
        print("1 - Взять меч" + "\n" + "2 - Пройти мимо меча")
        a = get_int_input([1, 2])
        if not 1 <= a <= 2:
            print("Введенное число не находится в диапазоне возможных значений")
            return 0
        if a == 1:
            knight['strenght'] = sword
            return knight['strenght']
        if a == 2:
            break


def random_choice():
    return random.choice


def take_apple():
    knight['health'] += apple
    print("Вы нашли яблочко! Ваше количество жизней =" + ' ' + str(knight['health']) + "\n")


def take_mech():
    print("Сила меча =" + " " + str(sword))
    input_sword()
    print("Сила рыцаря равна" + " " + str(knight['strenght']) + "\n")


def random_ch():
    count = 0
    while True:
        if knight['health'] <= 0:
            print("Игра окончена!")
            break
        if random.choice(sol) == "apple":
            take_apple()
        if random.choice(sol) == 'mech':
            take_mech()
        if random.choice(sol) == "enemy":
            print("Вы встретили чудовище c " + str(enemy['health']) + " жизнями и с силой удара " + str(enemy['strenght']))
            count += fight(count)
        if count >= 10:
            print("Вы победили! УРА!")
            break


def fight_step():
    current_enemy['health'] = current_enemy['health'] - knight['strenght']
    knight['health'] = knight['health'] - current_enemy['strenght']


def fight(count):
    while True:
        print("1 - Атака врага, 2 - Убежать от врага")
        a = get_int_input([1, 2])
        is_win = 0
        if a == 1:
            print(knight['strenght'])
            print("Атакуем врага!", "Ваше здоровье перед атакой равно " + " " + str(knight['health']))
            print("Атакуем врага!", "Ваша сила перед атакой равна " + " " + str(knight['strenght']))
            current_enemy['health'] = enemy['health']
            current_enemy['strenght'] = enemy['strenght']
            while True:
                if knight['health'] > 0:
                    if current_enemy['health'] > 0:
                        fight_step()
                    else:
                        print("Количество убитых вами врагов" + " " + str(count))
                        is_win = 1
                        break
                else:
                    break
            print("Здоровье после боя " + " " + str(knight['health']))
        if a == 2:
            print("Убегаем от врага")
        return is_win


random_ch()
