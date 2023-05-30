phone_book: list[dict[str, str]] = []
path = 'phone.txt'


def open_phonebook():
    global phone_book, path
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(":")
        phone_book.append({'name':  contact[0], 'phone': contact[1]})


def save_phonebook():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book


def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')


def delete_contact(index: int):
    return phone_book.pop(index-1).get('name')


def change_contact(index: int, contact: dict[str, str]):
    global phone_book
    phone_book[index-1] = contact
    return phone_book[index-1].get('name')


def find_contact(find: str):
    global phone_book, path
    with open(path, 'r', encoding='utf-8') as file:
        read_data = file.readlines()
        for letters in read_data:
            if find in letters:
                res = letters.strip()
    return res