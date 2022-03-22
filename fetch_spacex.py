import requests
from main import get_request, save_pic, SPACEX_LINK


def fetch_spacex_last_launch():
    try:
        response = get_request(SPACEX_LINK)
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from SPACEX server:\n{0}".format(error))
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)