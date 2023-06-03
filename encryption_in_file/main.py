import pyAesCrypt
import os

# вводим пароль для зашифровоного файла
password = input('Введите пароль: ')
# Вводим текст который мы хотим зашифровать

text = input('введите текст: ')

# Вводим путь и название для зашивровоного файла с нашим текстом
# по умолчанию будет добавлено расширение .txt.aes

file_crypt = input('Введите путь для создания файла: ')
# Записываем ранее введённый текст в простой текстовый файл
# (его необязательно отображать, он нужен только для того, что бы библиотека
# зашифровала текст и этот файл будет далее удалён)
with open('text.txt', 'w') as file:
    file.write(text)

# Шифруем введённый текст и сохраняем шифровку в файл, название которого ввели ранее
pyAesCrypt.encryptFile('text.txt', f'{file_crypt}.txt.aes', password)
print(f'Ваш текст зашифрован в файл {file_crypt}.txt.aes')
# Удаляем файл с первоначальным текстом
if os.path.exists('text.txt'):
    os.remove('text.txt')
# Спрашиваем хочет ли пользователь расшифровать файл
decrypt = input('Хотите рашифровать файл? ')
# дешифруем файл
if decrypt == "да":
    # Проверяем пароль
    password1 = input('Введите пароль: ')
    # Вводим путь к файлу, который хотим расшифровать
    file_decrypto = input('Введите путь к файлу: ')
    # Если пароль верный происходит расшифровка файла в путь указаный ранее
    if password1 == password:
        decrypt_out = input('Введите путь для файла с рашифровкой: ')
        pyAesCrypt.decryptFile(f'{file_decrypto}', f'{decrypt_out}.txt', password1)
        print(f'Файл с рашифровкой сохранён {decrypt_out}.txt')
        # Читаем и выводим в консоль расшифрованные данные
        with open(f'{decrypt_out}.txt', 'r') as file:
            file_reed = file.read()
        print(f'Ваш текст: {file_reed}')
    # Если пароль неверный завершаем программу
    else:
        print('Неверный пароль')
    # Спрашиваем удалить ли файл с расшифрованной информацией
    delete_decrypto_out = input('Удалить файл с раcшифровкой? ')
    if delete_decrypto_out == 'да':
        if os.path.exists(f'{decrypt_out}.txt'):
            os.remove(f'{decrypt_out}.txt')
            print('Файл с рашифрованным текстом удалён')
    else:
        print('Процесс завершен')
else:
    print('Процесс завершен')
