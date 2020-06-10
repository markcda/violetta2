#!/usr/bin/env python3

version = '0.0.3'

import sys
import os.path

translations = {
    'print': 'вывести',
    'input': 'ввести',
    'if': 'если',
    'elif': 'инесли',
    'else': 'иначе',
    'for': 'для',
    'in': 'в',
    'range': 'диапазон',
    'while': 'пока',
    'continue': 'продолжить',
    'break': 'прервать',
    'True': 'Истина',
    'False': 'Ложь',
    'None': 'Ничто',
    'type': 'тип',
    'str': 'строка',
    'int': 'целое',
    'float': 'дробное',
    'list': 'список',
    'tuple': 'кортеж',
    'dict': 'словарь',
    'bool': 'логический',
    'eval': 'определить',
    'exec': 'выполнить',
    'len': 'длина',
    'try': 'попробовать',
    'except': 'исключая',
    'finally': 'окончательно',
    'def': 'задать',
    'pass': 'пропустить',
    'return': 'вернуть',
    'del': 'удалить',
    'not': 'не',
    'and': 'и',
    'or': 'или',
    'is': 'есть',
    'isinstance': 'экземпляр',
    'min': 'минимум',
    'max': 'максимум',
    'from': 'из',
    'import': 'импортировать',
    'as': 'как',
    'global': 'глобально',
    'assert': 'заявить',
    'yield': 'предоставить',
    'lambda': 'лямбда',
    'raise': 'поднять',
    'exit': 'выйти',
    # работа с данными
    'append': 'дополнить',
    'remove': 'удалить',
    'insert': 'вставить',
    'items': 'элементы',
    # работа с классами
    'class': 'класс',
    'super': 'высший',
    # работа с файлами
    'open': 'открыть',
    'write': 'записать',
    'close': 'закрыть'
}


def shell():
    """Интерактивный режим Violetta2."""
    while True:
        print('Выберите опцию:')
        print('0. Выход')
        print('1. Преобразовать код Python 3 в псевдокод Violetta2')
        print('2. Преобразовать псевдокод Violetta2 в код Python 3')
        try:
            opt = int(input('>>> '))
            if opt not in (0, 1, 2):
                raise ValueError
            if opt == 1:
                print('\tВведите имя файла, содержащего код на Python 3:')
                filename = input('\t>>> ')
                toVioletta2(filename)
                print('\tПреобразование завершено.')
            elif opt == 2:
                print('\tВведите имя файла, содержащего псевдокод Violetta2:')
                filename = input('\t>>> ')
                toPython3(filename)
                print('\tПреобразование завершено.')
            else:
                return
        except ValueError:
            print('Ошибка! Введите число, соответствующее опции.')
        except KeyboardInterrupt:
            print()
            break


def toPython3(filepath):
    """Преобразует файл с именем filepath в код Python 3."""
    f = opener(filepath)
    strings = [line for line in f]
    f.close()
    writer(filepath, replace(strings, {v: k for k, v in translations.items()}), '.py')


def toVioletta2(filepath):
    """Преобразует файл с именем filepath в псевдокод Violetta2."""
    f = opener(filepath)
    strings = [line for line in f]
    f.close()
    writer(filepath, replace(strings, translations), '.vio2')


def opener(filepath):
    """Открывает файл и возвращает его."""
    try:
        f = open(filepath)
        return f
    except FileNotFoundError:
        print('Такого файла не существует.')
        sys.exit(1)


def writer(sourcefilepath, strings, extension):
    """Записывает изменения в файл."""
    try:
        newpath = os.path.split(sourcefilepath)[0] + os.path.splitext(sourcefilepath)[0][ len(os.path.split(sourcefilepath)[0]) : ] + extension
        with open(newpath, 'w') as f:
            for string in strings:
                f.write(string)
    except PermissionError:
        print('Ошибка записи в файл. Файловая система доступна только для чтения.')
        sys.exit(2)


def replace(strings, dictionary):
    """Производит преобразования кода в псевдокод или обратно."""
    replaced = []
    for string in strings:
        string = ' ' + string + ' '
        for key in dictionary.keys():
            shift = 0
            index = string.find(key, shift)
            while index != -1:
                if not string[index - 1].isalnum() and not string[index + len(key)].isalnum():
                    string = string[ : index] + dictionary[key] + string[index + len(key) : ]
                shift += len(key)
                index = string.find(key, shift)
        string = string[1 : -1]
        replaced.append(string)
    return replaced


def about():
    """Вывод информации о программе."""
    print(f'Транслятор Violetta2 v{version}. Вы пишете программу на "русском" Python, а транслятор переводит её в код Python на английском.\n\n\tИспользование: ./Violetta2.py [OPTIONS] FILEPATH\n\tОпции:\n\t\t-h, --help: выводит это сообщение\n\t\t--to-python3: транслирует файл в код на Python\n\t\t--to-violetta2: транслирует файл в код на Violetta2')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        shell()
    elif len(sys.argv) == 2 and sys.argv[1] != '-h' and sys.argv[1] != '--help':
        toPython3(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] == '--to-python3':
            toPython3(sys.argv[2])
        elif sys.argv[1] == '--to-violetta2':
            toVioletta2(sys.argv[2])
    else:
        about()
