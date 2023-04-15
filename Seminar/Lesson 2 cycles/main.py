# my_limit = int(input("Введите предел факториала: "))
#
# result = 1
# count = 1
# while count <= my_limit:
#     result *= count
#     count += 1
# print(f"Ответ: {my_limit}! = {result}")


# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# number = int(input("Введите число: "))
# count = 0
# n1 = 0
# n2 = 1
#
# while n2 < number:
#     n1, n2 = n2, n2 + n1
#     count += 1
# if number == 0:
#     print(0)
# elif n2 != number:
#     print("-1")
# else:
#     print(count + 1)


# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.

# import random
#
# lenght = 20
# i = 0
# count = 0
# result = 0
# day = 0
#
# while i < 20:
#     day += random.randint(-3, 3)
#     if day > 0:
#         count += 1
#         if count > result:
#             result = count
#     else:
#         count = 0
#     i += 1
#     print(day, end=" ")
# print(f"\nНаибольшее количество теплых дней подряд: {result}")


# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.

import random

MAX_WEIGHT = 8000
MIN_WEIGHT = 1000

min_weight = 0
max_weight = 1000
watermelons = int(input("Введите количество арбузов: "))
watermelons_weight = 1000

for i in range(watermelons):
    watermelons_weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
    if i == 0:
        min_weight = watermelons_weight
    if watermelons_weight > max_weight:
        max_weight = watermelons_weight
    if watermelons_weight < min_weight:
        min_weight = watermelons_weight

print(f"Самый тяжелый арбуз весит: {max_weight}гр. \nСамый легкий арбуз весит: {min_weight}гр.")
