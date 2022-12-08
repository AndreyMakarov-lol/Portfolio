# Подключение библиотек
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


# Функция отвечающая за обработку файлов
def pdf_to_mp3(file_path='test.pdf', language='en'):
    # Проверка того что файл подходит по параметрам
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # Описание рабочего окружения
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')
        # Открытие файла
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        # Убираем из файла перехода между страницами и переноса строк
        text = ''.join(pages)
        text = text.replace('\n', '')
        # Переработка текста в аудио и сохранение мп3 файла
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        # отчёт об успешном завершении
        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'
    # Вывод ошибки если файл не подходит
    else:
        return "The file doesn't exist, check the file path!"


# Главная функция отвечающая за вызов всех остальных функций
def main():
    tprint('PDF>TO>MP3', font='block', chr_ignore=True)
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    while language not in ("en", "ru"):
        language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))


# Функция запуска приложения
if __name__ == '__main__':
    main()
