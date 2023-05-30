main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Записать файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта'

save_successful = 'Сохранение прошло успешно!'

load_error = 'Телефонная книга пуста или не открыта'

input_contact = {'name': 'Введите имя: ', 'phone': 'Введите телефон: '}

new_contact = 'Введите данные нового контакта: '

oops = 'Для отмены, нажмите "Enter", предварительно сделав поле для заполнения пустым'


def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'


def delete_contact(name: str):
    return f'Контакт {name} успешно удален!'


def change_cont(name: str):
    return f'Контакт {name} успешно изменен!'


def found_contact(result):
    return f'Найден контакт: {result}'


cancel_input = 'Ошибка ввода'

index_delete_contact = 'Введите индекс контакта, который хотите удалить: '

index_change_contact = 'Введите индекс контакта, который хотите изменить: '

change_contact_m = 'Введите новые данные'

reminder = 'Не забудьте сохранить изменения'

find = 'Введите для поиска совпадений: '

