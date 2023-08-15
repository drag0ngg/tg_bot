import telebot

# Замените 'YOUR_TOKEN' на ваш токен, полученный от @BotFather
TOKEN = '5856102085:AAGw9tk4S5iIzglqFFM6zWJq3CN6u29-ksY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    response = 'ты лох'
    bot.reply_to(message, response)

@bot.message_handler(func=lambda message: True)
def respond_to_tvoia(message):
    if 'твоя' in message.text.lower():
        response = 'твоя?'
        bot.reply_to(message, response)

    if 'нет твоя' in message.text.lower():
        response = 'ну ок если твоя'
        bot.reply_to(message, response)

    if 'ты' in message.text.lower():
        response = 'ты?'
        bot.reply_to(message, response)

bot.polling()
