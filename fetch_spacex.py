from main import get_request, save_pic


def fetch_spacex_last_launch(spacex_link):
    response = get_request(spacex_link)
    spacex_links = response.json()['links']['flickr_images']
    for number, pic_url in enumerate(spacex_links):
        pic_path = f"images/SpaceX{number}.jpeg"
        save_pic(pic_url, pic_path)