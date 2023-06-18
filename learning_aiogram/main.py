# Импортируем необходимые библиотеки
from aiogram import Bot, Dispatcher, executor, types, filters
import os

# Инициализируем бота, используем токен из виртуального окружения
bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher(bot)

# Создаем Inline Keyboar (кнопки отображаются в самом диалоге)
inline_buttons = types.InlineKeyboardMarkup()

b1=types.InlineKeyboardButton(text='one', callback_data='send_one')  # атрибут callback_data='send' обратная связь при нажатии кнопки
b2=types.InlineKeyboardButton(text='two', callback_data='send_two')
b3=types.InlineKeyboardButton(text='no', callback_data='break')

# Добавляем кнопки к клавиатуре
inline_buttons.add(b1, b2)
# последнюю кнопку добавляем отдельной строкой
inline_buttons.row(b3)

# создаем клавиатуру
kb = types.ReplyKeyboardMarkup(resize_keyboard=True)  # клавиатура не самоудаляющаяся с кнопками автоматически подгоняемыми под размер текста

# Создаём кнопки
buttonslist = [types.KeyboardButton(text="mem"),
types.KeyboardButton(text='Send phone number', request_contact=True), # При нажатии кнопки пользователю предлагается отправить боту свой контакт
types.KeyboardButton(text='start3')]
# Добавляем кнопки к клавиатуре
kb.add(*buttonslist)


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
# @dp.message_handler()
async def echo(message: types.Message):
    # Из API вытаскиваем id и username пользователя
    user_id = message.from_user.id
    user_name = message.from_user.username
    await message.reply(f'Hi {user_id}, {user_name}')
    # Одна из вариации отправки сообщения пользователю
    await bot.send_message(chat_id=message.from_user.id, text="Hello")


# Реакци на нажате кнопки через фильтр отправляемого сообщения при нажатии этой кнопки
@dp.message_handler(filters.Text(contains="mem"))
async def cmd_handler(message: types.Message):
    # Ответ на нажатие кнопки
    await message.answer("Hi, it is butttom mem", reply_markup=inline_buttons)


# Обработка отправленного пользователем контакта
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def audio_handler(message: types.Message):
    await message.answer('Number save', reply_markup=types.ReplyKeyboardRemove()) # """Конструкция reply_markup=types.ReplyKeyboardRemove()
                                                                                # скрывает ранее вызванную клавиатуру после отправки боту контакта"""
# Обработка обратной связи при нажатии кнопки InlineKeyboar
@dp.callback_query_handler(filters.Text(contains="send_one"))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer('lovi')
    # Обратная связь телеграмму о том, что кнопка отработала
    await callback_query.answer()

# Обработка обратной связи при нажатии кнопки InlineKeyboar кнопки "send_two"
@dp.callback_query_handler(filters.Text(contains="send_two"))
async def some_callback_handler(callback_query: types.CallbackQuery):
    # Создаем медиа объект
    media = types.MediaGroup()
    # Добавляем к медиа группе 2 изображение(первое из католога, второе из интеренета)
    media.attach_photo(photo=types.InputFile('img/1.jpg'), caption='pervoe')
    media.attach_photo(photo='https://docs.aiogram.dev/en/latest/_static/logo.png', caption='vtoroe')
    #  Отправляем в ответ на нажатие кнопки медиа группу
    await callback_query.message.answer_media_group(media=media)
    # Реализуем другой метод отравки медиа файлов
    listphoto = [types.InputMediaPhoto(types.InputFile('img/2.png'), caption="esco"),
                types.InputMediaPhoto(types.InputFile('img/1.jpg'), caption="esco"),
                types.InputMediaPhoto('https://docs.aiogram.dev/en/latest/_static/logo.png')]
    await callback_query.message.answer_media_group(listphoto)
    # Обратная связь телеграмму о том, что кнопка отработала
    await callback_query.answer()

if __name__ == '__main__':
    # Запускаем нашего бота
    executor.start_polling(dp, skip_updates=True)
