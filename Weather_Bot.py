import telebot

API_TOKEN = '7093337586:AAFvNFOKuRAtpBiwiFPneDIEc4nYD5qnIZ8'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    button = telebot.types.KeyboardButton('Открыть веб старницу', web_app=telebot.types.WebAppInfo(url='https://github.com/ShelkZero'))
    markup.add(button)
    bot.send_message(message.chat.id, 'Привет, мой друг!', reply_markup=markup)
        
bot.infinity_polling()