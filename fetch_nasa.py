import os
import random
from datetime import datetime
from urllib.parse import urlparse

import requests
from dotenv import dotenv_values

from save_pictures import save_pic


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def fetch_nasa_apod(nasa_api_key):
    nasa_apod_link = f"https://api.nasa.gov/planetary/apod"
    count = random.randint(30, 50)
    payload = {"count": count, "api_key": nasa_api_key}
    nasa_links = requests.get(nasa_apod_link, params=payload)
    nasa_links.raise_for_status()
    for number, apod in enumerate(nasa_links.json()):
        pic_url = apod["url"]
        pic_extension = get_file_extension(pic_url)
        pic_path = f"images/NASA_APOD/NASA{number}{pic_extension}"
        directory = os.path.dirname(pic_path)
        os.makedirs(directory, exist_ok=True)
        try:
            save_pic(pic_url, pic_path, params=payload)
        except requests.exceptions.HTTPError as error:
            exit("Failed to save image:\n{0}".format(error))


def fetch_nasa_epic(nasa_api_key):
    nasa_epic_link = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": nasa_api_key}
    epic_pictures = requests.get(nasa_epic_link, params=payload)
    epic_pictures.raise_for_status()
    for number, picture in enumerate(epic_pictures.json()):
        pic_name = picture["image"]
        date = picture["date"]
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date = date.strftime("%Y/%m/%d")
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}" \
                  f"/png/{pic_name}.png"
        pic_path = f"images/NASA_EPIC/{pic_name}.png"
        directory = os.path.dirname(pic_path)
        os.makedirs(directory, exist_ok=True)
        try:
            save_pic(pic_url, pic_path, params=payload)
        except requests.exceptions.HTTPError as error:
            exit("Failed to save image:\n{0}".format(error))


if __name__ == '__main__':
    nasa_api_key = dotenv_values(".env")["NASA_API_KEY"]
    try:
        fetch_nasa_epic(nasa_api_key)
        fetch_nasa_apod(nasa_api_key)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA EPIC or APOD server:\n{0}".format(error))
