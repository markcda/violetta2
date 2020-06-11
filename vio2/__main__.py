#!/usr/bin/env python

version = '0.1.4'

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
    'map': 'карта',
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
    '.append': '.дополнить',
    '.remove': '.удалить',
    '.insert': '.вставить',
    '.items': '.элементы',
    '.split': '.разделить',
    '.keys': '.ключи',
    # работа с классами
    'class': 'класс',
    'super': 'высший',
    # работа с файлами
    'open': 'открыть',
    'write': 'записать',
    '.close': '.закрыть',
    'with': 'при помощи:'
}


def shell():
    """Интерактивный режим Violetta2."""
    while True:
        print('Выберите опцию:')
        print('0.  Выход')
        print('1.  Преобразовать код Python 3 в псевдокод Violetta2')
        print('2.  Преобразовать псевдокод Violetta2 в код Python 3')
        try:
            opt = int(input('>>> '))
            if opt not in (0, 1, 2):
                raise ValueError
            if opt == 1:
                print('Введите имя файла, содержащего код на Python 3:')
                filename = input('>>> ')
                toVioletta2(filename)
                print('Преобразование завершено.')
            elif opt == 2:
                print('Введите имя файла, содержащего псевдокод Violetta2:')
                filename = input('>>> ')
                toPython3(filename)
                print('Преобразование завершено.')
            else:
                return
        except ValueError:
            print('Ошибка! Введите число, соответствующее опции.')
        except KeyboardInterrupt:
            print()
            break


def toPython3(filepath):
    """Преобразует файл с именем filepath в код Python 3."""
    with opener(filepath) as f:
        strings = [line for line in f]
    writer(filepath, replace(strings, {v: k for k, v in translations.items()}), '.py')


def toVioletta2(filepath):
    """Преобразует файл с именем filepath в псевдокод Violetta2."""
    with opener(filepath) as f:
        strings = [line for line in f]
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
        newpath = os.path.split(sourcefilepath)[0] + os.path.splitext(sourcefilepath)[0][len(os.path.split(sourcefilepath)[0]):] + extension
        with open(newpath, 'w') as f:
            for string in strings:
                f.write(string)
    except PermissionError:
        print('Ошибка записи в файл. Файловая система доступна только для чтения.')
        sys.exit(2)


def find_quotes(string, opened, lastIndex):
    quotes = []
    for index in range(1, len(string) - 2):
        if string[index] in ('\'', '"'):
            if string[index - 1] == '\\':
                continue
            if opened is True:
                quotes.append((lastIndex, index - 1))
                opened = False
            else:
                lastIndex = index
                opened = True
        if not opened and string[index] == '#':
            quotes.append((index, len(string) - 2))
            break
    if opened and lastIndex == -1:  # говорит о том, что кавычки были открыты на другой строке
        return -1, opened, lastIndex
    return quotes, opened, lastIndex


def index_in_quotes(shift, index, key, string, quotes):
    for rn in quotes:
        if rn[0] <= index <= rn[1]:
            shift = index + len(key)
            index = string.find(key, shift)
            return True, shift, index
    return False, shift, index


def replace(strings, dictionary):
    """Производит преобразования кода в псевдокод или обратно."""
    replaced = []  # список строк исходного кода
    opened = False
    for string in strings:
        string = ' ' + string + ' '
        # stack = []
        lastIndex = -1
        # теперь можно заменять всё остальное
        for key in dictionary.keys():
            shift = 0
            index = string.find(key, shift)
            while index != -1:
                fq = find_quotes(string, opened, lastIndex)
                if fq[0] != -1:
                    quotes = fq[0]
                    opened = fq[1]
                    lastIndex = fq[2]
                else:
                    break
                iiq = index_in_quotes(shift, index, key, string, quotes)
                if iiq[0] is True:
                    shift = iiq[1]
                    index = iiq[2]
                    continue
                if (not string[index - 1].isalnum() and not string[index + len(key)].isalnum()) or (key[0] == '.' and not string[index + len(key)].isalnum()):
                    string = string[:index] + dictionary[key] + string[index + len(key):]
                shift = index + len(dictionary[key])
                index = string.find(key, shift)
        replaced.append(string[1:-1])
    return replaced


def about():
    """Вывод информации о программе."""
    print(f'Транслятор Violetta2 (v{version}). Вы пишете программу на "русском" Python, а транслятор переводит её в код Python на английском, и обратно.\n\n\tИспользование: ./vio2.py [OPTIONS] FILEPATH\n\tОпции:\n\t\t-h, --help: выводит это сообщение\n\t\t-p, --to-python3: транслирует файл в код на Python [опция по умолчанию]\n\t\t-v, --to-violetta2: транслирует файл в код на Violetta2')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        shell()
    elif len(sys.argv) == 2 and sys.argv[1] != '-h' and sys.argv[1] != '--help':
        toPython3(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] in ('-p', '--to-python3'):
            toPython3(sys.argv[2])
        elif sys.argv[1] in ('-v', '--to-violetta2'):
            toVioletta2(sys.argv[2])
    else:
        about()
