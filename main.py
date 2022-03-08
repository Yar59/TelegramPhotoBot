import os
import random
from urllib.parse import urlparse

import requests
from dotenv import dotenv_values


NASA_API_KEY = dotenv_values(".env")["NASA_API_KEY"]


def get_request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))


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


def fetch_spacex_last_launch(spacex_link):
    response = get_request(spacex_link)
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)


def fetch_nasa_apod(link):
    count = int(random.randrange(30, 50))
    count_params = {"count": count}
    nasa_links = get_request(link, params=count_params).json()
    for number, apod in enumerate(nasa_links):
        pic_url = apod["url"]
        pic_extension = get_file_extension(pic_url)
        pic_path = f"images/NASA_APOD/NASA{number}{pic_extension}"
        save_pic(pic_url, pic_path)


def fetch_nasa_epic(link):
    epic_pictures = get_request(link).json()
    for number, picture in enumerate(epic_pictures):
        pic_name = picture["image"]
        year = pic_name[8:12]
        month = pic_name[12:14]
        day = pic_name[14:16]
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}" \
                  f"/png/{pic_name}.png?api_key={NASA_API_KEY}"
        pic_path = f"images/NASA_EPIC/{pic_name}.png"
        save_pic(pic_url, pic_path)


def get_file_extension(link):
    return os.path.splitext(urlparse(link).path)[1]


def main():
    nasa_apod_link = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    nasa_epic_link = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_API_KEY}"
    pic_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    pic_path = "images/hubble.jpeg"
    spacex_link = "https://api.spacexdata.com/v3/launches/67"
    save_pic(pic_url, pic_path, headers={'Api-User-Agent': 'Example/1.0'})
    fetch_spacex_last_launch(spacex_link)
    fetch_nasa_apod(nasa_apod_link)
    fetch_nasa_epic(nasa_epic_link)


if __name__ == '__main__':
    main()
