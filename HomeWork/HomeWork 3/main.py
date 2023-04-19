#  Объединенная задача

# import random
#
# n = int(input("Введите количество чисел в списке: "))
# desired_num = int(input("Введите искомое число: "))
# count = 0
# nearest_num = 0
# difference = 1000000
#
# list_numb = [random.randint(1, 100) for i in range(n)]
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


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.


scrabble_en = {'A': '1', 'E': '1', 'I': '1', 'O': '1', 'U': '1', 'L': '1', 'N': '1', 'S': '1', 'T': '1', 'R': '1',
               'D': '2', 'G': '2', 'B': '3', 'C': '3', 'M': '3', 'P': '3', 'F': '4', 'H': '4', 'V': '4', 'W': '4',
               'Y': '4', 'K': '5', 'J': '8', 'X': '8', 'Q': '10', 'Z': '10'}
scrabble_ru = {'А': '1', 'В': '1', 'Е': '1', 'И': '1', 'Н': '1', 'О': '1', 'Р': '1', 'С': '1', 'Т': '1', 'Д': '2',
               'К': '2', 'Л': '2', 'М': '2', 'П': '2', 'У': '2', 'Б': '3', 'Г': '3', 'Ё': '3', 'Ь': '3', 'Я': '3',
               'Й': '4', 'Ы': '4', 'Ж': '5', 'З': '5', 'Х': '5', 'Ц': '5', 'Ч': '5', 'Ш': '8', 'Э': '8', 'Ю': '8',
               'Ф': '10', 'Щ': '10', 'Ъ': '10'}
points_list = []
points = 0

print(word := input("Введите слово: "), list(word))

for i in range(len(word)):
    if not word[i] in scrabble_en:
        print(scrabble_ru[list(word)[i]], end=" ")
        points_list += scrabble_ru[list(word)[i]]
        points += int(points_list[i])

    else:
        print(scrabble_en[list(word)[i]], end=" ")
        points_list += scrabble_en[list(word)[i]]
        points += int(points_list[i])

print(f"\n{points}")