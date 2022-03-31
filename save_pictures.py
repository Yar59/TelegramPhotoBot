import os
import requests


def save_pic(pic_url, pic_path, headers=None):
    if headers is None:
        headers = {}
    picture = requests.get(pic_url, headers=headers)
    directory = os.path.dirname(pic_path)
    os.makedirs(directory, exist_ok=True)
    with open(pic_path, 'wb') as file:
        file.write(picture.content)
