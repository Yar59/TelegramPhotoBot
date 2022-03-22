import random
import requests

from main import get_request, save_pic, get_file_extension, NASA_API_KEY
from main import NASA_APOD_LINK, NASA_EPIC_LINK


def fetch_nasa_apod():
    try:
        count = int(random.randrange(30, 50))
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-APOD server:\n{0}".format(error))
    count_params = {"count": count}
    nasa_links = get_request(NASA_APOD_LINK, params=count_params).json()
    for number, apod in enumerate(nasa_links):
        pic_url = apod["url"]
        pic_extension = get_file_extension(pic_url)
        pic_path = f"images/NASA_APOD/NASA{number}{pic_extension}"
        save_pic(pic_url, pic_path)


def fetch_nasa_epic():
    try:
        epic_pictures = get_request(NASA_EPIC_LINK).json()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from NASA-EPIC server:\n{0}".format(error))
    for number, picture in enumerate(epic_pictures):
        pic_name = picture["image"]
        year = pic_name[8:12]
        month = pic_name[12:14]
        day = pic_name[14:16]
        pic_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}" \
                  f"/png/{pic_name}.png?api_key={NASA_API_KEY}"
        pic_path = f"images/NASA_EPIC/{pic_name}.png"
        save_pic(pic_url, pic_path)