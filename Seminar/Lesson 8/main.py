# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


path = "Phonebook.txt"


def add_contact():
    with open(path, 'a', encoding='utf-8') as data:
        last_name = input("Введите фамилию: ").capitalize()
        first_name = input("Введите имя: ").capitalize()
        middle_name = input("Введите отчество: ").capitalize()
        phonenumber = input("Введите номер телефона: ")
        data.write(f"\n{last_name} {first_name} {middle_name} {phonenumber}\n")
    delete_empty_string()

def show_contacts():
    with open(path, 'r', encoding='utf-8') as data:
        print("Контакты:")
        for line in data:
            print(line.strip())


def find_contact():
    with open(path, 'r', encoding='utf-8') as data:
        find = input("Введите искомый параметр: ").capitalize()
        read_data = data.readlines()
        print("Вот, что мы нашли:")
        for letters in read_data:
            if find in letters:
                print(letters.strip())


def change_contact():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        old_data = data.read()
    print("Введите фамилию, имя, отчество или номер полностью, чтобы редактировать.", sep='\n')
    print(" Соблюдайте заглавные и прописные буквы.", sep='\n')
    new_data = old_data.replace(input("Введите информацию, которую хотите изменить: "),
                                input("Введите новый вариант: "))
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write(new_data)
    delete_empty_string()


def remove_contact():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        old_data = data.read()
    print("Введите фамилию, имя, отчество, номер или всю информацию о контакте, чтобы удалить.", sep='\n')
    print(" Соблюдайте заглавные и прописные буквы.", sep='\n')
    print("Удалится только та информация, которая будет введена.", sep='\n')
    new_data = old_data.replace(input("Введите информацию, которую хотите удалить: "), " ")
    with open('Phonebook.txt', 'w', encoding='utf-8') as data:
        data.write(new_data)
    delete_empty_string()


def delete_empty_string():
    with open(path, 'r', encoding='utf-8') as data:
        read_data = data.readlines()
    with open(path, 'w', encoding='utf-8') as data:
        for letters in read_data:
            if letters == "":
                data.write('')
    with open(path, 'a', encoding='utf-8') as data:
        for i in read_data:
            if i.strip() != "":
                data.write(i)


def menu():
    print("'1' - Посмотреть контакты")
    print("'2' - Добавить")
    print("'3' - Найти")
    print("'4' - Изменить контакт")
    print("'5' - Удалить контакт")
    print("'6' - Выход")
    print()

    while True:
        action = int(input("Действие: "))
        if action == 1:
            show_contacts()
        elif action == 2:
            add_contact()
        elif action == 3:
            find_contact()
        elif action == 4:
            change_contact()
        elif action == 5:
            remove_contact()
        elif action == 6:
            break


menu()

# Травников Дуб Лесович 89834432513
# Верин Владислав Олегович 89887556633
# Космосова Звезда Небовна 89873424651
# Чистова Грязнуля Уборковна 89873336725