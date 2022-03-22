import random
from main import get_request, save_pic, get_file_extension, NASA_API_KEY


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