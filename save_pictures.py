import os
import requests


def save_pic(pic_url, pic_path, headers=None):
    picture = requests.get(pic_url, headers=headers)
    check_folder(pic_path)
    with open(pic_path, 'wb') as file:
        file.write(picture.content)


def check_folder(pic_path):
    directory = os.path.dirname(pic_path)
    os.makedirs(directory, exist_ok=True)
    