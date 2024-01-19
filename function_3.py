import random
import numpy as np


def input_array_3():
    input_type = input("\nВыберите тип ввода данных:\n"
                       "1. вручную\n"
                       "2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        array_1 = np.array([int(x) for x in input("Введите первый массив чисел через пробел: ").split()])
        array_2 = np.array([int(x) for x in input("Введите второй массив чисел через пробел: ").split()])

    elif input_type == '2':
        n = int(input("Введите длину первого массива: "))
        array_1 = np.array([random.randint(0, 100) for _ in range(n)])
        m = int(input("Введите длину второго массива: "))
        array_2 = np.array([random.randint(0, 100) for _ in range(m)])
        print("Первый массив:", array_1)
        print("Второй массив:", array_2)

    else:
        print("Неверный тип ввода данных")
        array_1 = None
        array_2 = None

    return array_1, array_2


def task_3(array_1, array_2):
    cnt = 0
    for number in array_1:
        if (number in array_2) or (str(number)[::-1] in array_2):
            cnt += 1
    return cnt



