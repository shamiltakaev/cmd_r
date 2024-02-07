from io import BytesIO
import requests
from PIL import Image

apikey = "40d1649f-0493-4b70-98ba-98533de7710b"

def get_toponym(find_address):
    url = "http://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": apikey,
        "geocode": find_address,
        "format": "json",
        "result": 1
    }

    response = requests.get(url, params=params)
    if response:
        res_json = response.json()
        toponym = res_json["response"]["GeoObjectCollection"]["featureMember"]
        return toponym[0]["GeoObject"] if toponym else None
    
   
def get_ll_span(find_address):
    toponym = get_toponym(find_address=find_address)
    if toponym:
        coords = toponym["Point"]["pos"]
        ll = ",".join(coords.split())

        rect = toponym["boundedBy"]["Envelope"]
        left, bot = map(float, rect["lowerCorner"].split())
        right, top = map(float, rect["upperCorner"].split())

        dx = abs(left - right) / 2.5
        dy = abs(top - bot) / 2.5
        span = f"{dx},{dy}"
        return ll, span   

def show_map(find_address, map_type="map", add_params=None):
    ll, spn = get_ll_span(find_address=find_address)
    params = {
        "ll": ll,
        "spn": spn,
        "l": map_type,
        "pt": ll
    }
    api_server = "http://static-maps.yandex.ru/1.x/"

    response = requests.get(api_server, params=params)
    Image.open(BytesIO(response.content)).show()

show_map("Грозный", "map")
