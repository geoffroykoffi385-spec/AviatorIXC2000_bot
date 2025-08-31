import telebot
import random

TOKEN = "TON_TOKEN_TELEGRAM_ICI"
bot = telebot.TeleBot(TOKEN)7643663995:AAGYNoHObgEUHsmxCRYFwOd_BqNCjHP4xME

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Bienvenue dans Aviator Predictor Bot !")

@bot.message_handler(commands=['predict'])
def predict(message):
    prediction = round(random.uniform(1.2, 10.0), 2)
    bot.reply_to(message, f"🎯 Prochaine prédiction : {prediction}x")

print("Bot lancé...")
bot.polling()
