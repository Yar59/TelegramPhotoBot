import os
import random
from urllib.parse import urlparse
from datetime import datetime
import requests

from main import NASA_API_KEY
from save_pictures import save_pic


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def fetch_nasa_apod():
    nasa_apod_link = f"https://api.nasa.gov/planetary/apod"
    count = int(random.randrange(30, 50))
    payload = {"count": count, "api_key": NASA_API_KEY}
    nasa_links = requests.get(nasa_apod_link, params=payload).json()
    for number, apod in enumerate(nasa_links):
        pic_url = apod["url"]
        pic_extension = get_file_extension(pic_url)
        pic_path = f"images/NASA_APOD/NASA{number}{pic_extension}"
        save_pic(pic_url, pic_path)


def fetch_nasa_epic():
    nasa_epic_link = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": NASA_API_KEY}
    epic_pictures = requests.get(nasa_epic_link, params=payload).json()
    for number, picture in enumerate(epic_pictures):
        pic_name = picture["image"]
        date = picture["date"]
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date = date.strftime("%Y/%m/%d")
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}" \
                  f"/png/{pic_name}.png?api_key={NASA_API_KEY}"
        pic_path = f"images/NASA_EPIC/{pic_name}.png"
        save_pic(pic_url, pic_path)


if __name__ == '__main__':
    try:
        fetch_nasa_epic()
        fetch_nasa_apod()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-EPIC server:\n{0}".format(error))
