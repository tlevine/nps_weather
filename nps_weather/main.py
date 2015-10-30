from .download import get
from . import parse

WEATHER = 'http://www.nps.gov/%(id)s/planyourvisit/weather.htm'

def nps_weather():
    parks = parse.findapark(get('http://www.nps.gov/findapark/index.htm'))
    for park in parks:
        response = get(WEATHER % park)
        if parse.has_weather(response):
            weather = parse.weather(response)
            if weather:
                park['weather'] = weather
        yield park
