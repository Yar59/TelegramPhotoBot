import os
import random
from urllib.parse import urlparse

import requests

from main import NASA_APOD_LINK, NASA_EPIC_LINK, NASA_API_KEY


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


def fetch_nasa_apod():
    count = int(random.randrange(30, 50))
    count_params = {"count": count}
    nasa_links = get_request(NASA_APOD_LINK, params=count_params).json()
    for number, apod in enumerate(nasa_links):
        pic_url = apod["url"]
        pic_extension = get_file_extension(pic_url)
        pic_path = f"images/NASA_APOD/NASA{number}{pic_extension}"
        save_pic(pic_url, pic_path)


def fetch_nasa_epic():
    epic_pictures = get_request(NASA_EPIC_LINK).json()
    for number, picture in enumerate(epic_pictures):
        pic_name = picture["image"]
        year = pic_name[8:12]
        month = pic_name[12:14]
        day = pic_name[14:16]
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}" \
                  f"/png/{pic_name}.png?api_key={NASA_API_KEY}"
        pic_path = f"images/NASA_EPIC/{pic_name}.png"
        save_pic(pic_url, pic_path)


if __name__ == '__main__':
    try:
        fetch_nasa_epic()
        fetch_nasa_apod()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-EPIC server:\n{0}".format(error))
