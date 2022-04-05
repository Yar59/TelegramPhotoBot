import os
from time import sleep

import telegram
from dotenv import dotenv_values


def post_endlessly(bot, chat_id, posting_period):
    while True:
        for root, dirs, files in os.walk("images"):
            for filename in files:
                image_path = f"{root}/{filename}"
                with open(image_path, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id=chat_id, photo=photo)
                sleep(float(posting_period))


if __name__ == '__main__':
    tg_token = dotenv_values(".env")["TG_TOKEN"]
    chat_id = dotenv_values(".env")["CHAT_ID"]
    posting_period = dotenv_values(".env")["POSTING_PERIOD"]
    bot = telegram.Bot(token=tg_token)
    post_endlessly(bot, chat_id, posting_period)
