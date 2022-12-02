import telebot
from telebot import types

bot = telebot.TeleBot('5856730850:AAFNfRgPmwHe59am4d2Bbdhbnyy6lssdgik')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    help = types.KeyboardButton('да')
    start = types.KeyboardButton('нет')
    markup.add(help, start)
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'Хочешь увидеть самую красивую девочку на свете?', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "помощь для педиков", parse_mode='html')


@bot.message_handler(commands=['web'])
def web(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Hei', url="https://www.youtube.com/"))
    bot.send_message(message.chat.id, 'gay', reply_markup=markup)


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    help = types.KeyboardButton('да')
    start = types.KeyboardButton('нет')
    markup.add(help, start)
    bot.send_message(message.chat.id, '', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'да':
        bot.send_message(message.chat.id, 'вот она', parse_mode='html')
        photo = open('9R4gtZ4ZqFo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'you id {message.from_user.id}', parse_mode='html')
    elif message.text == 'рот твой топтал':
        photo = open('Fq1SC4p_lic.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'i dont', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'good photo')


bot.polling(none_stop=True)
