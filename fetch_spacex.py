import requests

from save_pictures import save_pic


def fetch_spacex_last_launch():
    spacex_link = "https://api.spacexdata.com/v3/launches/67"
    response = requests.get(spacex_link)
    response.raise_for_status
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)


if __name__ == '__main__':
    try:
        fetch_spacex_last_launch()
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from SPACEX server:\n{0}".format(error))
