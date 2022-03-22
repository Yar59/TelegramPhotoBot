import os
from urllib.parse import urlparse
from time import sleep

import requests
import telegram
from dotenv import dotenv_values


from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic
from fetch_spacex import fetch_spacex_last_launch


NASA_API_KEY = dotenv_values(".env")["NASA_API_KEY"]
TG_TOKEN = dotenv_values(".env")["TG_TOKEN"]
CHAT_ID = dotenv_values(".env")["CHAT_ID"]
POSTING_PERIOD = dotenv_values(".env")["POSTING_PERIOD"]
NASA_APOD_LINK = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
NASA_EPIC_LINK = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API_KEY}"
SPACEX_LINK = "https://api.spacexdata.com/v3/launches/67"


def get_request(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response


def save_pic(pic_url, pic_path, headers=None):
    if headers is None:
        headers = {}
    picture = get_request(pic_url, headers=headers)
    check_folder(pic_path)
    with open(pic_path, 'wb') as file:
        file.write(picture.content)


def check_folder(pic_path):
    directory = os.path.dirname(pic_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def infinity_posting(bot):
    while True:
        for address, dirs, files in os.walk("images"):
            for file in files:
                image = address+'/'+file
                bot.send_photo(chat_id=CHAT_ID, photo=open(image, "rb"))
                sleep(float(POSTING_PERIOD))


def main():
    bot = telegram.Bot(token=TG_TOKEN)
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epic()
    infinity_posting(bot)


if __name__ == '__main__':
    main()
