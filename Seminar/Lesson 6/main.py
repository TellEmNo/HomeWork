# 39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве

from random import randint


# def new_list():
#     print()
#     minn = int(input("Введите нижний предел: "))
#     maxx = int(input("Введите верхний предел: "))
#     lenght = int(input("Введите длину списка: "))
#     print()
#     new_list1 = [randint(minn, maxx) for i in range(lenght)]
#
#     return new_list1

# # Решение в лоб

# def comparison(list1, list2):
#     i = 0
#     while i <= len(list2) - 1:
#         for j in range(len(list1)):
#             if list2[i] == list1[j]:
#                 list1.pop(j)
#                 i -= 1
#                 break
#         if i == len(list2) - 1:
#             return list1
#         i += 1
#
# # Нормальное решение
#
# def comparison(list1, list2):
#     uniq_list = []
#     for i in list1:
#         if i not in list2:
#             uniq_list.append(i)
#     return uniq_list


# list1 = new_list()
# print(list1)
# list2 = new_list()
# print(list2)
# print(comparison(list1, list2))

# list comprehension

# uniq_ = [i for i in list1 if i not in list2]
# print(uniq_)


# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.

# list_of_numbers = [randint(0, 100) for i in range(20)]
# print(list_of_numbers)
#
# # Обычное решение
#
# def little_neighbors(list1):
#     count = 0
#     for i in range(1, len(list1) - 1):
#         if list1[i - 1] < list1[i] > list1[i + 1]:
#             count += 1
#     return count
#
#
# print(f"Количество элементов, больших, чем соседние: {little_neighbors(list_of_numbers)}")
#
# # list comprehension

# count = [1 for i in range(1, len(list_of_numbers) - 1) if list_of_numbers[i - 1] < list_of_numbers[i] > list_of_numbers[i + 1]]

# print(f"Количество элементов, больших, чем соседние: {len(count)}")


# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# list1 = [randint(0, 10) for i in range(20)]
# print(list1)

# pairs = sum([list1.count(i) // 2 for i in set(list1)])
# # проходим по значениям множества и узнаем количество вхождений в список и целочисленно делим его на 2

# print(pairs)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.


def dividers(k):
    set_of_divisor_sums = {}
    for i in range(2, k + 1):
        basket = 0
        for j in range(1, i//2 + 1):
            if i % j == 0:
                basket += j
        set_of_divisor_sums[i] = basket
    for i in range(2, len(set_of_divisor_sums) + 1):
        if set_of_divisor_sums[i] == 1:
            del set_of_divisor_sums[i]
    return set_of_divisor_sums


def friendly_numbers(divisor: dict, k):
    res_list = []
    for i in divisor.keys():
        for j in divisor.keys():
            if i == divisor[j] and j == divisor[i] and i != divisor[i]:
                res_list.append(f"{i} = {divisor[i]}")
                # print(f"{i} = {divisor[j]}, {j} = {divisor[i]}")
    return res_list


k = 10**4
div = dividers(k)
print(f"Дружественные числа: {friendly_numbers(div, k)}")