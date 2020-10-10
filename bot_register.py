import config
import telebot
from telebot import types
from string import Template

bot = telebot.TeleBot('1254205987:AAEQ2b81-l0RDLvImd_3kZUflK_NpRu8MCc')
user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 'driverNumber', 'driverDate',
                'car', 'carModel', 'carColor', 'carNumber','carDate']
        for i in keys:
            self.i = None

@bot.message_handler(commands=['help','start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/aboutus')
    itembtn2 = types.KeyboardButton('/register')
    itembtn3 = types.KeyboardButton('/register2')
    markup.add(itembtn1,itembtn2,itembtn3)

    bot.send_message(message.chat.id, "Assalomu alaykum"+" "+message.from_user.first_name+
                     ",men botman, sizga qanday yordam berishim mumkin?",reply_markup=markup)
@bot.message_handler(commands=['aboutus'])
def send_about(message):
    bot.send_message(message.chat.id, "Biz ishonchli korxona hisoblanamiz! Biz 5 yildan buyon bozordamiz!")

@bot.message_handler(commands=['register'])
def user_register(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Tashkent')
    itembtn2 = types.KeyboardButton('Qarshi')
    itembtn3 = types.KeyboardButton('Samarqand')
    markup.add(itembtn1, itembtn2, itembtn3)
    msg = bot.send_message(message.chat.id, 'Sizning shahar?', reply_markup=markup)
    bot.register_next_step_handler(msg, proccess_city_step)

def proccess_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Familya ism sharifingiz!', reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_fullname_step)
    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')

def proccess_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Telefon raqamingiz!')
        bot.register_next_step_handler(msg, proccess_phone_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz, +9989x-xxx-xx-xx bilan kiriting')

def proccess_phone_step(message):
    try:
        int(message.text)
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Haydovchilik guvohnomangiz seriya raqami!')
        bot.register_next_step_handler(msg, proccess_driverSeria_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Siz telefon raqamingizni xato kiritdingiz! Iltimos boshqatdan kiriting')
        bot.register_next_step_handler(msg, proccess_phone_step)
def proccess_driverSeria_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverSeria = message.text

        msg = bot.send_message(chat_id, 'Haydovchilik guvohnomasi davlat raqami!')
        bot.register_next_step_handler(msg, proccess_driverNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')

def proccess_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text

        msg = bot.send_message(chat_id, 'Haydovchilik guvohnomasi berilgan sanasi. Kun Oy Yil !')
        bot.register_next_step_handler(msg, proccess_driverDate_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')
def proccess_driverDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Avtomobil markasini kiriting !')
        bot.register_next_step_handler(msg, proccess_car_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')
def proccess_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Avtomobil modelini kiriting !')
        bot.register_next_step_handler(msg, proccess_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')
def proccess_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Oq rang')
        itembtn2 = types.KeyboardButton('Qora')
        itembtn3 = types.KeyboardButton('Kulrang')
        markup.add(itembtn1, itembtn2, itembtn3)

        msg = bot.send_message(chat_id, 'Avtomobil rangini tanlang!', reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')

def proccess_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(chat_id, 'Avtomobil davlat raqamini kiriting !', reply_markup=markup)
        bot.register_next_step_handler(msg, proccess_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')
def proccess_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Avtomobil ishlab chiqarilgan yil !')
        bot.register_next_step_handler(msg, proccess_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'Xato kiritdingiz!')
def proccess_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        bot.send_message(chat_id, getRegData(user, 'Sizning arizangiz qabul qilindi', message.from_user.first_name),parse_mode="Markdown")
        bot.send_message(config.chat_id, getRegData(user, 'bot tomonidan tayyorlangan ariza!', bot.get_me().username),parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'Sizning davlat raqamingiz!')

def getRegData(user, title, name):
    t = Template('$title *$name*\n Shahar: *$city*\n FISH: *$fullname*\n Telefon:*$phone* \n HGSR: *$driverSeria*\n HGDR: *$driverNumber* \n HGBS: *$driverDate* \n Marka: *$car* \n Model: *$carModel* \n Rangi: *$carColor*, \n ADR: *$carNumber* \n AICHY: *$carDate*')

    return t.substitute({
        'title':title,
        'name':name,
        'city': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria,
        'driverNumber': user.driverNumber,
        'driverDate': user.driverDate,
        'car':user.car,
        'carModel': user.carModel,
        'carColor':user.carColor,
        'carNumber':user.carNumber,
        'carDate': user.carDate,

    })

@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'Biz haqimizda-/aboutus \n Registratsiya - /register \n Yordam - /help')

@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, "Matn kiriting!:")
bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()
bot.callback_query_handlers.clear()
if __name__=='__main__':
    bot.polling(none_stop=True)

while True: # Don't end the main thread.
    pass