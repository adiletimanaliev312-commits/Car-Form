import telebot
from telebot import types

# 🔑 Вставь сюда свой токен от BotFather
TOKEN = "ВСТАВЬ_СВОЙ_ТОКЕН_СЮДА"
bot = telebot.TeleBot(TOKEN)

# Словарь для временного хранения данных пользователей
user_data = {}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Оставить заявку 🚗")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     "Здравствуйте! 👋\nЭтот бот создан компанией TLV Auto для удобства клиентов.\n"
                     "Здесь вы можете оставить заявку, и наши специалисты с вами свяжутся.",
                     reply_markup=markup)

# При нажатии кнопки "Оставить заявку 🚗"
@bot.message_handler(func=lambda message: message.text == "Оставить заявку 🚗")
def ask_name(message):
    bot.send_message(message.chat.id, "Введите ваше имя:")
    bot.register_next_step_handler(message, ask_phone)

def ask_phone(message):
    user_data[message.chat.id] = {"name": message.text}
    bot.send_message(message.chat.id, "Введите ваш номер телефона:")
    bot.register_next_step_handler(message, ask_brand)

def ask_brand(message):
    user_data[message.chat.id]["phone"] = message.text
    bot.send_message(message.chat.id, "Введите марку автомобиля (например: Toyota):")
    bot.register_next_step_handler(message, ask_model)

def ask_model(message):
    user_data[message.chat.id]["brand"] = message.text
    bot.send_message(message.chat.id, "Введите модель автомобиля (например: Camry):")
    bot.register_next_step_handler(message, ask_year)

def ask_year(message):
    user_data[message.chat.id]["model"] = message.text
    bot.send_message(message.chat.id, "Введите год выпуска автомобиля:")
    bot.register_next_step_handler(message, ask_budget)

def ask_budget(message):
    user_data[message.chat.id]["year"] = message.text
    bot.send_message(message._
