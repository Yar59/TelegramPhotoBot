import os
from time import sleep

import telegram
from dotenv import dotenv_values


NASA_API_KEY = dotenv_values(".env")["NASA_API_KEY"]
TG_TOKEN = dotenv_values(".env")["TG_TOKEN"]
CHAT_ID = dotenv_values(".env")["CHAT_ID"]
POSTING_PERIOD = dotenv_values(".env")["POSTING_PERIOD"]


def post_endlessly(bot):
    while True:
        for root, dirs, files in os.walk("images"):
            for filename in files:
                image_path = f"{root}/{filename}"
                with open(image_path, "rb") as file:
                    photo = file.read()
                bot.send_photo(chat_id=CHAT_ID, photo=photo)
                sleep(float(POSTING_PERIOD))


def main():
    bot = telegram.Bot(token=TG_TOKEN)
    post_endlessly(bot)


if __name__ == '__main__':
    NASA_API_KEY = dotenv_values(".env")["NASA_API_KEY"]
    TG_TOKEN = dotenv_values(".env")["TG_TOKEN"]
    CHAT_ID = dotenv_values(".env")["CHAT_ID"]
    POSTING_PERIOD = dotenv_values(".env")["POSTING_PERIOD"]
    main()
