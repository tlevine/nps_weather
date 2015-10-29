from .download import get
from . import parse

WEATHER = 'http://www.nps.gov/%s/planyourvisit/weather.htm'

def nps_weather():
    park_identifiers = parse.findapark(get('http://www.nps.gov/findapark/index.htm'))
    for park_identifier in park_identifiers:
        yield parse.weather(get(WEATHER % park_identifier))
