# Импортируем необходимые библиотеки
from aiogram import Bot, Dispatcher, executor, types
import os

# Инициализируем бота, используем токен из виртуального окружения
bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher(bot)

# создаем клавиатуру
kb = types.ReplyKeyboardMarkup(resize_keyboard=True) # клавиатура не самоудаляющаяся с кнопками автоматически подгоняемыми под размер текста

# Создаём кнопки
b1 = types.KeyboardButton(text='start1')
b2 = types.KeyboardButton(text='start2')
b3 = types.KeyboardButton(text='start3')
# Добавляем кнопки к клавиатуре
kb.add(b1, b2, b3)


@dp.message_handler(commands=['start'])
async def cmd_handler(message: types.Message):
    # Отправка сообщения с прикрепленной клавиатурой
    await message.answer("Hi", reply_markup=kb)


# Обработка команд  'welcome', 'about' и ответ на них
@dp.message_handler(commands=['welcome', 'about'])
async def cmd_handler(message: types.Message):
    # Из данных телеграмма вытаскиваем first_name пользователя
    user_first_name = message.from_user.first_name
    # Отвечаем пользователю с указанием его first_name
    await message.answer(f'hi {user_first_name}, i`am bot')


# Обработка сообщения состоящего из слова hello
@dp.message_handler(lambda message: message.text and 'hello' in message.text.lower())
# Обработка сообщения в которое изменением добавили слово hello
@dp.edited_message_handler(lambda message: message.text and 'hello' in message.text.lower())
async def msg_handler(message: types.Message):
    await message.answer('И тебе здорова сталкер')


# Обработка и ответ на отправку боту фотографиии
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def audio_handler(message: types.Message):
    await message.answer('Kakoe krasivoe foto')


# Обработка текстового сообщения без определённых параметров
@dp.message_handler()
async def echo(message: types.Message):
    # Из API вытаскиваем id и username пользователя
    user_id = message.from_user.id
    user_name = message.from_user.username
    await message.reply(f'Hi {user_id}, {user_name}')
    # Одна из вариации отправки сообщения пользователю
    await bot.send_message(chat_id=message.from_user.id, text="Hello")


if __name__ == '__main__':
    # Запускаем нашего бота
    executor.start_polling(dp, skip_updates=True)
