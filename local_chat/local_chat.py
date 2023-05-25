from flask import Flask, request, render_template  # импортируем фласк, предварительно устанавливаем pip install flask
from datetime import datetime
import json
import os

app = Flask(__name__)  # Создаем экземпляр приложения
DB_FILE_NAME = 'db.json'


# json.dump - загрузка в файл
# json.load - чтение из файла

def load_messages():
    # Проверка существования файла базы сообщений или он пустой то возвращение пустого списка
    if not os.path.exists(DB_FILE_NAME) or not os.path.getsize(DB_FILE_NAME) > 0:
        return []
    with open(DB_FILE_NAME, "r") as file:
        data = json.load(file)
    return data.get("messages", [])


all_messages = load_messages()


def add_message(author, text):  # объявляем функцию добавления сообщений с параметрами
    message = {
        "author": author,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    all_messages.append(message)  # добавляем параметризированное сообщение в список всех сообщений
    save_message()


def save_message():  # сохраняем сообщения в файл
    all_messages_data = {
        "messages": all_messages
    }
    with open("db.json", "w") as file:
        json.dump(all_messages_data, file)


@app.route("/")  # реализуем эндпоинт начальной страницы
def main_page():
    return chat_page()


@app.route("/chat")
def chat_page():
    return render_template("form.html")


@app.route("/get_messages")
def get_messages():
    print("Отдаем все сообщения")
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    name = request.args.get("name")  # получаем данные из query параметров запроса к серверу
    text = request.args.get("text")
    print(f"пользователь '{name}' пишет '{text}'")
    add_message(name, text)
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # конфигурируем параметры запуска приложения
