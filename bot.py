from bs4 import BeautifulSoup
import requests
import telebot
import random
import schedule
import time

me = "<SIZNI TELEGRAM ID iz>" # int qiymatda

bot = telebot.TeleBot("<SIZNI API TOKENIZ>")
def getRandomHadith():
    url = "https://islom.ziyouz.com/hadis/islomning-o-zagi-bo-lgan-hadislar"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    div = soup.find("div", class_="item-page")
    h = div.findAll("p")

    hadith = []
    for i in h:
        hadith.append(i.text)

    bot.send_message(me, random.choice(hadith))

schedule.every(1).minutes.do(getRandomHadith)

while True:
    schedule.run_pending()
    time.sleep(1)




# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     rh = random.choice(hadith)
#     bot.reply_to(message, f"{rh}")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# bot.polling()

