from function_1 import input_array_1
from function_1 import task_1
from function_2 import input_array_2
from function_2 import task_2
from function_3 import input_array_3
from function_3 import task_3


def display_result(result):
    if result is not None:
        print("Результат:", result)
    else:
        print("Исходные данные не введены")


def main():

    array_1, array_2, array_3 = None, None, None

    while True:
        print("\nМеню:")
        print("1. Выбор задания")
        print("2. Ввод исходных данных")
        print("3. Выполнение алгоритма по заданию")
        print("4. Вывод результата алгоритма")
        print("5. Завершение работы программы")

        point = input("\nВведите пункт меню: ")

        if point == "1":
            print(
                "\n1. Три массива с числами одинакового размера. Нужно проверить, могут ли два числа под одним и тем "
                "же номером в сумме давать третье число."
                "\nЕсли могут, то сумма трех чисел возводится в степень наименьшего числа.")
            print(
                "2. Два массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или "
                "разность массивов.")
            print("3. Два массива с числами. Требуется проверить, сколько у массивов общих чисел."
                  "\nТакже, число будет считаться общим, если оно входит в один массив, а в другом массиве находится "
                  "его перевернутая версия.")

            choice = input("\nВведите номер задания: ")

            if choice == "1":
                result = None
            elif choice == "2":
                result = None
            elif choice == "3":
                result = None
            else:
                print("Некорректный выбор задания.")

        elif point == "2":

            choice = input("Введите номер задания: ")

            if choice == "1":
                array_1, array_2, array_3 = input_array_1()
            elif choice == "2":
                array_1, array_2 = input_array_2()
            elif choice == "3":
                array_1, array_2 = input_array_3()
            else:
                print("Некорректный выбор задания.")

        elif point == "3":

            choice = input("Введите номер задания: ")

            if choice == "1":
                result = task_1(array_1, array_2, array_3)
            elif choice == "2":
                result = task_2(array_1, array_2)
            elif choice == "3":
                result = task_3(array_1, array_2)
            else:
                print("Некорректный выбор задания.")

        elif point == "4":
            display_result(result)

        elif point == "5":
            print("Программа завершена")
            break

        else:
            print("Выберите верный пункт меню")


if __name__ == "__main__":
    main()
