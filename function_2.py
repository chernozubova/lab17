import random
import numpy as np


def input_array_2():
    array_1 = None
    array_2 = None
    input_type = input("\nВыберите тип ввода данных:\n"
                       "1. вручную\n"
                       "2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        try:
            input_string_1 = input("Введите первый массив цифр через пробел: ")
            array_1 = np.array([int(x) for x in input_string_1.split() if x.isdigit()])
            array_1 = ''.join(map(str, array_1))
            input_string_2 = input("Введите первый массив цифр через пробел: ")
            array_2 = np.array([int(x) for x in input_string_2.split() if x.isdigit()])
            array_2 = ''.join(map(str, array_2))

        except ValueError:
            print("Неверный тип ввода данных")

    elif input_type == '2':
        n = int(input("Введите длину первого массива: "))
        index_1 = 0
        while index_1 == 0:
            array_1 = np.array([random.randint(0, 9) for _ in range(n)])
            index_1 = array_1[0]
        array_1 = ''.join(map(str, array_1))
        m = int(input("Введите длину второго массива: "))
        index_2 = 0
        while index_2 == 0:
            array_2 = np.array([random.randint(0, 9) for _ in range(m)])
            index_2 = array_2[0]
        array_2 = ''.join(map(str, array_2))
        print("Первый массив:", array_1)
        print("Второй массив:", array_2)

    else:
        print("Неверный тип ввода данных")
        array_1 = None
        array_2 = None

    return array_1, array_2


def task_2(array_1, array_2):
    input_type = input("\nВыберите операцию, которая будет выполнена над массивом:\n"
                       "1. сложение\n"
                       "2. вычитание\nВведите номер операции: ")
    if input_type == '1':
        result = int(array_1) + int(array_2)
    elif input_type == '2':
        result = int(array_1) - int(array_2)
    else:
        print("Неверный пункт")
        result = None

    return result
