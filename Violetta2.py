#!/usr/bin/env python3
# @titoffklim

version = '0.0.2'

# Подключаем библиотеки:
# 1) системная библиотека - понадобится для получения аргументов командной строки
import sys
# 2) библиотека для работы с путями в файловой системе
import os.path

# Все замены, которые мы делаем:
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

# Процедура shell, которая вызывается для интерактивного режима. Вы должны ввести путь к файлу, выбрать направление перевода, и транслятор переведёт ваш код, сохранив его в файле с таким же названием, но другим расширением.
def shell():
    pass

# Процедура toPython3, которая принимает filepath - путь к файлу, - открывает его, переводит, создаёт новый файл с расширением .py и записывает перевод.
def toPython3(filepath):
    f = opener(filepath)
    strings = [line for line in f]
    f.close()
    writer(filepath, replace(strings, {v: k for k, v in translations.items()}), '.py')

# Процедура toVioletta2, которая принимает filepath, открывает его, переводит, создаёт новый файл с расширением .vio2 и записывает перевод.
def toVioletta2(filepath):
    f = opener(filepath)
    strings = [line for line in f]
    f.close()
    writer(filepath, replace(strings, translations), '.vio2')    

def opener(filepath):
    try:
        f = open(filepath)
        return f
    except:
        print('Такого файла не существует.')
        sys.exit(1)

def writer(sourcefilepath, strings, extension):
    try:
        newpath = os.path.split(sourcefilepath)[0] + os.path.splitext(sourcefilepath)[0][ len(os.path.split(sourcefilepath)[0]) : ] + extension
        f = open(newpath, 'w')
        for string in strings:
            f.write(string)
        f.close()
    except:
        print('Ошибка записи в файл.')
        sys.exit(2)

def replace(strings, dictionary):
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

# О программе, как ей пользоваться.
def about():
    print(f'Транслятор Violetta2 v{version}. Вы пишете программу на "русском" Python, а транслятор переводит её в код на английском Python.\n\n\tИспользование: ./Violetta2.py [OPTIONS] FILEPATH\n\tОпции:\n\t\t-h, --help: выводит это сообщение\n\t\t--to-python3: транслирует файл в код на Python\n\t\t--to-violetta2: транслирует файл в код на Violetta2')

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
