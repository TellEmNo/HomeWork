#  Объединенная задача
#
# import random
#
# n = int(input("Введите количество чисел в списке: "))
# desired_num = int(input("Введите искомое число: "))
# count = 0
# nearest_num = 0
# difference = 1000000
#
# list_numb = [random.randint(1, 10) for i in range(n)]
# print(list_numb)
#
# for i in range(n):
#     if list_numb[i] == desired_num:
#         count += 1
#     elif abs(desired_num - list_numb[i]) < difference:
#         difference = abs(desired_num - list_numb[i])
#         nearest_num = list_numb[i]
#
# if count > 0:
#     print(f"Искомое число встречается: {count} раз/раза")
# else:
#     print(f"Ближайшее число: {nearest_num}")
#
# Вариант решения из 4 семинара
#
# import random
#
# size = int(input("Введите количество чисел в списке: "))
# max_limit = int(input("Введите верхний предел: "))
# min_limit = int(input("Введите нижний предел: "))
# desired_number = int(input("Введите искомое число: "))
# list_num = [random.randint(min_limit, max_limit) for i in range(size)]
# closest = list_num[len(list_num) - 1]
#
# print(list_num)
# count = list_num.count(desired_number)
#
# if count < 1:
#     for i in list_num:
#         if abs(desired_number - i) < abs(desired_number - closest):
#             closest = i
# print(f"Число {desired_number} встречается {count} раз/раза" if count >
#                                                                 0 else f"Ближайшее число к искомому: {closest}")
#
# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# scrabble_en = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1',
#                'D': '2', 'G': '2', 'B': '3', 'C': '3', 'M': '3', 'P': '3', 'F': '4', 'H': '4', 'V': '4', 'W': '4',
#                'Y': '4', 'K': '5', 'J': '8', 'X': '8', 'Q': '10', 'Z': '10'}
# scrabble_ru = {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1', 'Д': '2',
#                'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3',
#                'Й': '4', 'Ы': '4', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5', 'Ш': '8', 'Э': '8', 'Ю': '8',
#                'Ф': '10', 'Щ': '10', 'Ъ': '10'}
# points_list = []
# points = 0
#
# print(word := input("Введите слово: "), list(word))
#
# for i in range(len(word)):
#     if not word[i] in scrabble_en:
#         print(scrabble_ru[list(word)[i]], end=" ")
#         points_list += scrabble_ru[list(word)[i]]
#         points += int(points_list[i])
#
#     else:
#         print(scrabble_en[list(word)[i]], end=" ")
#         points_list += scrabble_en[list(word)[i]]
#         points += int(points_list[i])
#
# print(f"\n{points_list}")
# print(f"\n{points}")
#
# Вариант решения из 4 семинара
#
# scrabble = {"AEIOULNSTRАВЕИНОРСТ": 1,
#             "DGДКЛМПУ": 2,
#             "BCMPБГЁЬЯ": 3,
#             "FHVWYЙЫ": 4,
#             "KЖЗХЦЧ": 5,
#             "JXШЭЮ": 8,
#             "QZФЩЪ": 10}
#
# word = input("Введите слово: ")
# total = 0
#
# for letter in word.upper():
#     for letters in scrabble.keys():  # ... in scrabble: == ... in scrabble.keys():
#         if letter in letters:
#             total += scrabble.get(letters)
#             break
# print(f"Слово {word.upper()} набирает {total} баллов")
#
# Еще одно
#
# scrabble = {1: "AEIOULNSTRАВЕИНОРСТ",
#             2: "DGДКЛМПУ",
#             3: "BCMPБГЁЬЯ",
#             4: "FHVWYЙЫ",
#             5: "KЖЗХЦЧ",
#             8: "JXШЭЮ",
#             10: "QZФЩЪ"}
#
# word = input("Введите слово: ")
# total = 0
#
# for letter in word.upper():
#     for points, letters in scrabble.items():
#         if letter in letters:
#             total += points
#             break
# print(f"Слово {word.upper()} набирает {total} баллов")

# И еще одно

# my_dict = {}
#
# my_dict.update(my_dict.fromkeys("AEIOULNSTRАВЕИНОРСТ", 1))
# my_dict.update(my_dict.fromkeys("DGДКЛМПУ", 2))
# my_dict.update(my_dict.fromkeys("BCMPБГЁЬЯ", 3))
# my_dict.update(my_dict.fromkeys("FHVWYЙЫ", 4))
# my_dict.update(my_dict.fromkeys("KЖЗХЦЧ", 5))
# my_dict.update(my_dict.fromkeys("JXШЭЮ", 8))
# my_dict.update(my_dict.fromkeys("QZФЩЪ", 10))
#
# word = input("Введите слово: ")
# total = 0
#
# for letter in word.upper():
#     total += my_dict.get(letter)

# print(f"Слово {word.upper()} набирает {total} баллов")

# и еще

scrabble = [(1, "AEIOULNSTRАВЕИНОРСТ"),
            (2, "DGДКЛМПУ"),
            (3, "BCMPБГЁЬЯ"),
            (4, "FHVWYЙЫ"),
            (5, "KЖЗХЦЧ"),
            (8, "JXШЭЮ"),
            (10, "QZФЩЪ")]

my_dict = {}
[my_dict.update(my_dict.fromkeys(values, keys)) for keys, values in scrabble]

word = input("Введите слово: ")
total = 0

for letter in word.upper():
    total += my_dict.get(letter)

print(f"Слово {word.upper()} набирает {total} баллов")