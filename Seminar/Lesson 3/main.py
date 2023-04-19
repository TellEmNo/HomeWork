# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
#
# import random
#
# n = int(input("Введите количество чисел: "))
# list_numb = []
#
# for i in range(n):
#     list_numb.append(random.randint(1, 100))
# print(list_numb)
#
# q = set(list_numb)
# print(q)
#
# print(len(q))
#
# Еще вариант решения
#
# list_num = list(input("Введите числа: "))
#
# uniq_list = []
#
# for item in list_num:
#     if not item in uniq_list:  # in - проверка вхождения/не вхождения(not) в список
#         uniq_list.append(item)
# print(list_num)
# print(uniq_list)
# print(len(uniq_list))
#
# И еще
#
# list_num = list(input("Введите числа: "))
# print(list_num)
# print(len(set(list_num)))
#
# И еще
#
# print(set_num := input("Введите числа: "), len((set(set_num))))
#
#
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
#
# import random
#
# shift = int(input("Введите величину сдвига: "))
# n = int(input("Введите количество чисел: "))
# list_numb = []
#
# for i in range(n):
#     list_numb.append(random.randint(1, 100))
# print(list_numb)
#
# for i in range(shift):
#     list_numb.insert(0, list_numb.pop())
# print(list_numb)
#
# Другой вариант решения
#
# import random
#
# shift = int(input("Введите величину сдвига: "))
# n = int(input("Введите количество чисел: "))
# list_numb = []
#
# for i in range(n):
#     list_numb.append(random.randint(1, 100))
# print(list_numb)
#
# list_numb = list_numb[-shift:] + list_numb[:-shift]
# print(list_numb)
#
#
# Дан список, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
#
# import random
#
# n = int(input("Введите количество чисел: "))
# list_numb = []
# count = 0
#
# for i in range(n):
#     list_numb.append(random.randint(1, 100))
# print(list_numb)
#
# for i in range(len(list_numb) - 1):
#     if list_numb[i + 1] > list_numb[i]:
#         count += 1
# print(count)
#
#
# Напишите программу для печати всех уникальных значений в словаре.
#
# list_ = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009 "}, {" VIII": "S007 "}]
# print(list_)
# new_list = []
#
# for item in list_:
#     new_list += list(item.values())
#
# print(set(new_list))
#
# Другой вариант решения
#
# list_ = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009 "}, {" VIII": "S007 "}]
# print(list_)
# uniq_set = set()
#
# for item in list_:
#     for value in item.values():
#         uniq_set.add(value)
# print(uniq_set)