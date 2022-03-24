import os
from time import sleep

import telegram
from dotenv import dotenv_values


NASA_API_KEY = dotenv_values(".env")["NASA_API_KEY"]
TG_TOKEN = dotenv_values(".env")["TG_TOKEN"]
CHAT_ID = dotenv_values(".env")["CHAT_ID"]
POSTING_PERIOD = dotenv_values(".env")["POSTING_PERIOD"]
NASA_APOD_LINK = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
NASA_EPIC_LINK = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API_KEY}"
SPACEX_LINK = "https://api.spacexdata.com/v3/launches/67"


def post_endlessly(bot):
    while True:
        for root, dirs, files in os.walk("images"):
            for filename in files:
                image_path = f"{root}/{filename}"
                bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, "rb"))
                sleep(float(POSTING_PERIOD))


def main():
    bot = telegram.Bot(token=TG_TOKEN)
    post_endlessly(bot)


if __name__ == '__main__':
    main()
