import requests


def save_pic(pic_url, pic_path, headers=None, params=None):
    picture = requests.get(pic_url, headers=headers, params=params)
    picture.raise_for_status
    with open(pic_path, 'wb') as file:
        file.write(picture.content)
