# Импортируем необходимые библиотеки
from aiogram import Bot, Dispatcher, executor, types
import os
# Инициализируем бота, используем токен из виртуального окружения
bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher(bot)

# Обработка команд 'start', 'welcome', 'about' и ответ на них
@dp.message_handler(commands=['start', 'welcome', 'about'])
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


if __name__ == '__main__':
    # Запускаем нашего бота
    executor.start_polling(dp, skip_updates=True)
