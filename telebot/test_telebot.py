import telebot  #pyTelegramBotApi
import sqlite3
import sys

token = '5*************546546'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def starter(message):
    conn = sqlite3.connect(r'/home/red/PycharmProjects/python_belhard\us.db')
    cursor = conn.cursor()
    curselect = cursor.execute("""SELECT * FROM '{}'""".format('Users'))

    all_user = curselect.fetchall()

    # print( all_user[0] )
    # print (tuple((message.chat.id, message.from_user.first_name, message.from_user.last_name)))

    if tuple((str(message.chat.id), message.from_user.first_name, message.from_user.last_name)) not in all_user:
    # if  len(cursor.execute("SELECT * FROM Users WHERE  id = " + str(message.chat.id)).fetchall()) == 0:
        bot.send_message(message.chat.id, 'Hi! You are a new guy.')

        conn = sqlite3.connect(r'/home/red/PycharmProjects/python_belhard\us.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO Users VALUES('{}', '{}', '{}')""".format(message.chat.id, message.from_user.first_name,message.from_user.last_name))
        conn.commit()
        conn.close()
    else:
        bot.send_message(message.chat.id, 'hey!  what s up! what is new?')


@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    if message.photo:
        print(message.photo)
        print(sqlite3.Binary(message.photo))
        
        bot.send_message(message.chat.id, 'Красиво!')

        # try:
        #     conn = sqlite3.connect(r'/home/red/PycharmProjects/python_belhard\us.db')
        #     cursor = conn.cursor()
        #
        #     # data = readImage(message.photo)
        #     # Конвертируем данные
        #     binary = sqlite3.Binary(message.photo)
        #     print(binary)
        #     # Готовим запрос в базу
        #     # cursor.execute(("INSERT INTO Images(id, image) VALUES " + (message.chat.id,binary)))
        #     conn.commit()
        # except:
        #     print('error!')


@bot.message_handler(content_types=['text'])
def current_weather_bot(message):
    if message.text:
        print('<logging', message.chat.id, message.from_user.first_name,  message.from_user.last_name, 'mes_text: ' + message.text, sep='//')
        bot.send_message(message.chat.id, 'давай побеседуем!')
        bot.send_message(message.chat.id, 'Вот твой текст: ' + message.text)

@bot.message_handler(content_types=['location'])
def locator(message):
    if message.location:
        print('<logging', message.chat.id, message.from_user.first_name, message.from_user.last_name,'user_location: ' + str(message.location), sep='//')
        bot.send_message(message.chat.id, 'Твои координаты: ' + str(message.location.latitude) + 'x' + str(message.location.longitude))

@bot.message_handler(content_types=['sticker'])
def stickerer(message):
    if message.sticker:
        print(message.sticker.file_id)
        bot.send_message(message.chat.id, 'Не знаю, зачем мне стикер, но спасибо ***')
        # bot.send_sticker(message.chat.id, 'CAADAgADMgMAAsSraAsjlpGPjHteRAI')
        bot.send_sticker(message.chat.id, message.sticker.file_id)



bot.polling(none_stop=True)
