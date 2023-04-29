import csv
import telebot
import datetime as datetime

bot = telebot.TeleBot('5558718715:AAHlPCKabtoayvIt64Xcr-lBbUcYEjy6qcM')

count = 0

@bot.message_handler(commands=['start', 'help'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,f'Привет! \n Хочешь узнать кто у тебя сейчас за компьютером?)\n Тогда я тебе помогу\n Напиши "/камера"')
    else:
        bot.send_message(message.chat.id,f'сейчас скажу, только напиши "/камера"');
@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    with open("imena.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            if "/камера" in message.text:
                bot.reply_to(message, f'за компьютером сидит {row["Name"]}')
                print(f'{row["Name"]}')
                break
            else:
                bot.reply_to(message, "Неверный формат ввода. Напиши /help.")
                print(f'{row["Name"]}')
bot.polling(none_stop=True, interval=0)