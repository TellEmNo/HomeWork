# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# n = float(input('Введите, сколько километров машина проезжает за день: '))
# m = float(input('Введите длину маршрута: '))
# result = (m + n - 0.001) // n
#
# print(f"Ответ: {int(result)}")


# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# a = int(input("Введите количество учащихся А класса: "))
# b = int(input("Введите количество учащихся Б класса: "))
# c = int(input("Введите количество учащихся В класса: "))
#
# a1 = ((a + 1) // 2)
# b1 = ((b + 1) // 2)
# c1 = ((c + 1) // 2)
#
# result = a1 + b1 + c1
#
# print(f"Всего парт нужно приобрести: {result}")


# Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
# это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# i = int(input("Введите вагон от головы или хвоста поезда: "))
# j = int(input("Введите номер вагона: "))
#
# if i == j:
#     print("Не хватает условий!")
# else:
#     print(f"Вагонов: {i + j - 1}")


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")

