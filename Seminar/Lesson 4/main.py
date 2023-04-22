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

# text = list(input("Введите строку: "))
#
# count_dict = {}
#
# for char in text:
#     count_dict[char] = count_dict.get(char, -1) + 1
#     # через запятую указываем то, что нам нужно вывести, если нет искомого ключа
#     print(f"{char}" if count_dict.get(char) == 0 else f"{char}_{count_dict.get(char)}", end=" ")

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# my_string = input("Введите строку: ")
my_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper()
words = set()

for i in my_string.upper():
    words.update(my_string.split())
print(len(words))




