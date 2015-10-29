from .download import get
from . import parse

WEATHER = 'http://www.nps.gov/%(id)s/planyourvisit/weather.htm'

def nps_weather():
    parks = parse.findapark(get('http://www.nps.gov/findapark/index.htm'))
    for park in parks:
        parse.weather(get(WEATHER % park))
        print(park)
