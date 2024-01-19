import random
import math
import numpy as np


def input_array_1():
    input_type = input("\nВыберите тип ввода данных:\n"
                       "1. вручную\n"
                       "2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        array_1 = np.array([int(x) for x in input("Введите первый массив чисел через пробел: ").split()])
        array_2 = np.array([int(x) for x in input("Введите второй массив чисел через пробел: ").split()])
        array_3 = np.array([int(x) for x in input("Введите третий массив чисел через пробел: ").split()])

    elif input_type == '2':
        n = int(input("Введите длину массивов: "))
        array_1 = np.array([random.randint(0, 100) for _ in range(n)])
        array_2 = np.array([random.randint(0, 100) for _ in range(n)])
        array_3 = np.array([random.randint(0, 100) for _ in range(n)])
        print("Первый массив:", array_1)
        print("Второй массив:", array_2)
        print("Третий массив:", array_3)

    else:
        print("Неверный тип ввода данных")
        return None, None, None

    return array_1, array_2, array_3


def task_1(array_1, array_2, array_3):
    try:
        for i in range(len(array_1)):
            if array_1[i] + array_2[i] == array_3[i]:
                array_3[i] = math.pow(array_3[i], min(array_1[i], array_2[i]))
            else:
                print("Два числа под одним и тем же номером в сумме не дают третье число")
                return None
        return array_3
    except IndexError:
        print("Массивы разной длины")
        return None
