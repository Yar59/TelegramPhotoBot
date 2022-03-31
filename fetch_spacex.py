import os
import requests


def save_pic(pic_url, pic_path, headers=None):
    if headers is None:
        headers = {}
    picture = requests.get(pic_url, headers=headers)
    check_folder(pic_path)
    with open(pic_path, 'wb') as file:
        file.write(picture.content)


def check_folder(pic_path):
    directory = os.path.dirname(pic_path)
    os.makedirs(directory, exist_ok=True)


def fetch_spacex_last_launch():
    spacex_link = "https://api.spacexdata.com/v3/launches/67"
    response = requests.get(spacex_link)
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)


if __name__ == '__main__':
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from SPACEX server:\n{0}".format(error))
