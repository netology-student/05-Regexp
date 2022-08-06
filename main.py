# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pprint import pprint
import csv
import json
import re


def fix_fio(contact_list):
    # 1. Из первых трех элементов каждой строки вытаскиваем содержимое и разбиваем по пробелам
    # 2. Перезаписываем в каждой строке первые три элемента сформированными ФИО
    for rec in contacts_list:
        fio_strings = []
        for i in range(3):
            if (rec[i] != ''):
                splt = rec[i].split(' ')
                fio_strings.extend(splt)
        # pprint(fio_strings)

        for i in range(3):
            if i < len(fio_strings):
                rec[i] = fio_strings[i]
            else:
                rec[i] = ''

def fix_phones(contacts_list):
    # Выгружаем список в JSON, применяем регулярное, загружаем обратно
    text = json.dumps(contacts_list, ensure_ascii=False)
    pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    fixed_phones = re.sub(pattern_phone, r'+7(\2)\3-\4-\5\6\7\8', text)
    contacts_list = json.loads(fixed_phones)


def merge_contacts(contacts_list):
    # Группируем по ФИ
    groups = {}
    for rec in contacts_list:
        key = f'{rec[0]}{rec[1]}'
        if key in groups:
            groups[key].append(rec)
        else:
            groups[key] = [rec]

    contacts_list.clear()
    for value in groups.values():
        new_rec = ['','','','','','','']
        for rec in value:
            for i in range(len(new_rec)):
                if new_rec[i] == '' and rec[i] != '':
                    new_rec[i] = rec[i]
        contacts_list.append(new_rec)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        contacts_list.pop(0)

    # TODO 1: выполните пункты 1-3 ДЗ

    # 1
    fix_fio(contacts_list)
    # pprint(contacts_list)

    # 2
    fix_phones(contacts_list)
    # pprint(contacts_list)

    # 3
    merge_contacts(contacts_list)
    # pprint(contacts_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contacts_list)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
