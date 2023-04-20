# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# string_ = list(input("Введите что-то: "))
#
# for char in range(len(string_)):
#     count = string_[:char].count(string_[char])
#     if count == 0:
#         print(f"{string_[char]}", end=" ")
#     else:
#         print(f"{string_[char]}_{count}", end=" ")

# Альтернатива

text = list(input("Введите строку: "))

count_dict = {}

for char in text:
    count_dict[char] = count_dict.get(char, -1) + 1
    # через запятую указываем то, что нам нужно вывести, если нет искомого ключа
    print(f"{char}" if count_dict.get(char) == 0 else f"{char}_{count_dict.get(char)}", end=" ")