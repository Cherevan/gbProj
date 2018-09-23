import os
import psutil
import shutil
import sys
import random

MAIN_DIR = '/home/andriy/Dropbox/pure_python/test_dir/'
file_list = sorted(os.listdir(MAIN_DIR))


def duplicate_file(_userfile):
    _filename = os.path.join(MAIN_DIR, _userfile)
    _new_file = _filename + '.temp'
    if os.path.isfile(_filename):
        shutil.copy(_filename, _new_file)
        if os.path.exists(_new_file):
            print(f'Файл {_userfile}.temp було створено.')


def delete_files():
    file_list = sorted(os.listdir(MAIN_DIR))
    _count = 0
    for item in file_list:
        _file = os.path.join(MAIN_DIR, item)
        if _file.endswith('.temp'):
            os.remove(_file)
            if not os.path.exists(_file):
                _count += 1
                print(f'Файл {item} було видалено.')
    return _count


def sys_info():
    print('Поточна директорія:', os.getcwd())
    print('Операційна система:', os.uname())
    print('Кодування файлової системи:', sys.getfilesystemencoding())
    print('Ім\'я користувача', os.getlogin())
    print('Кількість CPU', psutil.cpu_count())


def copy_all():
    file_list = sorted(os.listdir(MAIN_DIR))
    for i in file_list:
        duplicate_file(i)


def rand_delete():
    file_list = sorted(os.listdir(MAIN_DIR))
    _rand = random.randrange(0, len(file_list))
    _file = os.path.join(MAIN_DIR, file_list[_rand])
    if os.path.isfile(_file):
        os.remove(_file)
        print(f'Файл {_file} було видалено.')


def main():
    print('Привіт. Ця програма - ваш домашній помічник.')
    key_words = ''

    while key_words != 0:
        file_list = sorted(os.listdir(MAIN_DIR))
        print('''================================
        Введіть цифру дії:
        [1] - вивести список файлів директорії на екран.
        [2] - вивсести інформацію про систему.
        [3] - вивсести список процесів на екран.
        [4] - стоврити резервні копії всіх файлів директорії.
        [5] - стоврити резервну копію вказаного файлу.
        [6] - видалити всі резервні копії файлів.
        [0] - вийти з програми.
    ================================''')

        try:
            key_words = int(input('Що ви хочете зробити?'))
        except ValueError:
            print('Введений символ не вірний')

        if key_words == 1:
            for i in range(len(file_list)):
                print('[' + str(i) + '] - ' + str(file_list[i]))
        elif key_words == 2:
            sys_info()
        elif key_words == 3:
            print(psutil.pids())
        elif key_words == 4:
            copy_all()
        elif key_words == 5:
            filename = int(input('Вкажіть індекс обраного файлу.'))
            duplicate_file(file_list[filename])
        elif key_words == 6:
            del_count = delete_files()
            print('Загалом видалено', del_count, 'файлів.')
        elif key_words == 0:
            pass
        else:
            print('Ви ввели невірну команду. Спробуйте ще раз.')


if __name__ == '__main__':
    main()
