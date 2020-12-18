
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