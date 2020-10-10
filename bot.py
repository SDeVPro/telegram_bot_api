import telebot

bot = telebot.TeleBot('1254205987:AAEQ2b81-l0RDLvImd_3kZUflK_NpRu8MCc')
keybord1 = telebot.types.ReplyKeyboardMarkup(True, True)
keybord1.row('Salom', 'Xayr','Salomat', 'Omonmisiz')
@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'Salom siz! /start ni bosdingiz!', reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id, 'Salom xush kelibsiz!')
    elif message.text.lower() == 'xayr':
        bot.send_message(message.chat.id, 'Xayr!')
    elif message.text.lower() == 'salomat':
        bot.send_message(message.chat.id, 'https://t.me/c/1313184419/315!')
    elif message.text.lower() == 'omonmisiz':
        bot.send_message(message.chat.id, 'https://t.me/c/1313184419/315!')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
