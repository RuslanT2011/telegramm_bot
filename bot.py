import telebot
import time, threading, schedule
from Kodland import gen_pass
bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "В этом боте есть команды: /start - начало бота, /hello - приветствие, /ping - проверка, работает ли бот, /set <seconds> - время, через которое сработает таймер, /unset - закончить таймер, /bye - прощание, /pass - генерация пароля")



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "Бот работает!") 

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['pass'])
def send_password(message):
    password=gen_pass(10)
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")


def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)


if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)  
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




bot.polling() 
