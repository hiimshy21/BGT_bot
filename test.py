import logging
import telebot
from telebot import types
from datetime import datetime, timedelta
import threading
import atexit


TOKEN = "6615785111:AAFpWnz34UMfGEjlQo-hiJ7rW-UTF9kQ7Oc"
GROUP_CHAT_ID = "-1001648678945" 
THREAD_ID= "6640"
USER_TO_TAG = "@hiimshy21"

bot = telebot.TeleBot(TOKEN)


def send_daily_message():
    now = datetime.now()
    now_text = now.strftime("%c")
    today_1_am = datetime(now.year, now.month, now.day, 20, 6)
    if now >= today_1_am:
        today_1_am += timedelta(days=1)
    time_until_next_run = (today_1_am - datetime.now()).total_seconds()
    threading.Timer(time_until_next_run, send_daily_message).start()
    message = f"Now:{now_text}\n Remind: Send BGT report!!!"
    bot.send_message(chat_id=GROUP_CHAT_ID,message_thread_id=THREAD_ID, text=message)

atexit.register(threading.Timer(0, send_daily_message).cancel)

def main():
    #send_daily_message()
    threading.Timer(1, send_daily_message).start()
    bot.polling()


if __name__ == "__main__":
    main()
