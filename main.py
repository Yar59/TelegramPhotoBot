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
    bot.send_message(text='Бот был перезагружен!', chat_id=CHAT_ID)
    nasa_apod_link = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    nasa_epic_link = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API_KEY}"
    pic_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    pic_path = "images/hubble.jpeg"
    spacex_link = "https://api.spacexdata.com/v3/launches/67"
    save_pic(pic_url, pic_path, headers={'Api-User-Agent': 'Example/1.0'})
    try:
        fetch_spacex_last_launch(spacex_link)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from SPACEX server:\n{0}".format(error))
    try:
        fetch_nasa_apod(nasa_apod_link)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-APOD server:\n{0}".format(error))
    try:
        fetch_nasa_epic(nasa_epic_link)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-EPIC server:\n{0}".format(error))
    infinity_posting(bot)


if __name__ == '__main__':
    main()
