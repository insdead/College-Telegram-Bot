import telebot
import random

from telebot import types

TOKEN = '1384946842:AAE_7ciGe2ziBxAmYCO7bY0O1CExvSCECsw'
bot = telebot.TeleBot(TOKEN)

stic = open('static/welcome.webp', 'rb')
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Arpi?")
	item2 = types.KeyboardButton("Ссылки")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать с поиском файлов. \nЕсли у вас есть полезные ресурсы чтобы поделиться, пишите сюда - @insdead".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Arpi?':
			bot.send_sticker(message.chat.id, stic)
		if message.text == 'Ссылки':
			bot.send_message(message.chat.id, 'ielts - https://drive.google.com/drive/u/0/folders/1dxqatNNM4cRKeaVpON2a0UHfgJsYVrzi \n\ncollege - https://drive.google.com/drive/folders/1CSYSxTWhDd5ALiUg1meFuQPSFtgUK9Xz \n\nNUFYPET - https://drive.google.com/drive/folders/1oRvs-_HuThgqIV7gJb6zs2VeUpdBA0y9 \n\nPractice math NUFYPET - https://drive.google.com/drive/folders/18IhCZdPKMY1A14HnjRjEJq9CEKBnQZDz \n\n1000+ College Admission Essay Samples - https://www.cracksat.net/college-admission/essays/ \n\nSAT real tests download - https://www.cracksat.net/index.html \n\nGeometry - https://drive.google.com/drive/folders/1ou9hl_w22GmkmCTzTpcEimu5LqtMxV7w \n\nNUFYPET thinking skills - https://drive.google.com/drive/u/0/folders/1wFk1t-6JA5Icc7bQDleehZrKp41mKIAa \n\nNIS A* - https://drive.google.com/drive/u/0/folders/173c5Kq-g7qeYFS-Q3fdmApsYnygT2yPN')
		else:
			bot.send_message(message.chat.id, 'Много Arpi не бывает')


# RUN
bot.polling(none_stop=True)