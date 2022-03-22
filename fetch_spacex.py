import os
import requests

from main import SPACEX_LINK


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


def fetch_spacex_last_launch():
    response = get_request(SPACEX_LINK)
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)


if __name__ == '__main__':
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from SPACEX server:\n{0}".format(error))
