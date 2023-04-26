# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random
#
# n = 30
# print(marks := list([random.randint(2, 5) for i in range(n)]))
#
# for index, mark in enumerate(marks):
#     if mark == max(marks):
#         marks[index] = min(marks)
# print(marks)

# for i in range(len(marks)):
#     if marks[i] == max(marks):
#         marks[i] = min(marks)
# print(marks)

# marks = [min(marks) if i == max(marks) else i for i in marks]
# print(marks)

# print([min(marks) if i == max(marks) else i for i in marks])


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.

# number = int(input("Введите число: "))
# def is_prime(num: int) -> bool:
#     if num in [1, 2]:
#         return True
#     # elif num % 2 == 0:   - то же, что и строкой ниже
#     elif not num % 2:
#         return False
#     for i in range(3, num//2+1, 2):
#         # if not num % i:  - то же, что и строкой ниже
#         if num % i == 0:
#             return False
#         return True
#
# print(f"Число {number}" + (" - простое" if is_prime(number) else " - составное"))


# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

# # print(sequence_n[-1])
# # print(sequence_n[:-1])
# def revers(n):
#     if len(n) == 1:
#         return n
#     return n[-1] + revers(n[:-1])
#
# sequence_n = input("Введите строку: ")
# print(revers(sequence_n))

def revers_list(n):
    return (1 if n == 1 else f"{n}, {revers_list(n-1)}")
num = int(input("Введите число n: "))
print(revers_list(num))