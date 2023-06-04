class PhoneBook:

    def __init__(self, path: str = 'phone.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    def open(self):
        with open(self._path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(":")
            new = {'name':  contact[0], 'phone': contact[1]}
            self._phone_book.append(new)

    def save(self):
        data = []
        for contact in self._phone_book:
            contact = ':'.join([value for value in contact.values()])
            data.append(contact)
        with open(self._path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(data))

    def load(self) -> list[dict[str, str]]:
        return self._phone_book

    def add(self, contact: dict[str, str]) -> str:
        self._last_id += 1
        contact['id'] = str(self._last_id)
        self._phone_book.append(contact)
        return contact.get('name')

    def delete(self, index: int):
        return self._phone_book.pop(index-1).get('name')

    def change(self, index: int, contact: dict[str, str]):
        self._phone_book[index-1] = contact
        return self._phone_book[index-1].get('name')

    def search(self, find: str):
        with open(self._path, 'r', encoding='utf-8') as file:
            read_data = file.readlines()
            for letters in read_data:
                if find in letters:
                    res = letters.strip()
        return res