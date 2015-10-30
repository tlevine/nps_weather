import re
from functools import reduce

import lxml.html

WEATHER = 'http://www.nps.gov/%s/planyourvisit/weather.htm'

def findapark(response):
    html = lxml.html.fromstring(response.content)
    options = html.xpath('//select[@name="alphacode"]/optgroup/option')
    for option in options:
        park_id = str(option.xpath('@value')[0])
        yield {
            'id': park_id,
            'name': str(option.xpath('text()')[0]),
            'url': WEATHER % park_id,
        }

SEASON = re.compile(r'.*(winter|spring|summer| fall|autumn).*', flags = re.IGNORECASE)
def weather(response):
    html = lxml.html.fromstring(response.content)
    containers = html.xpath('id("content-main-container")')
    if len(containers) == 1:
        def merge_small(ys, x):
            _ys = list(ys)
            if len(_ys[-1]) < 30:
                _ys[-1] += x
            else:
                _ys.append(x)
            return _ys
        lines = reduce(merge_small, containers[0].text_content().split('\n'), [''])
        return '\n\n'.join(line.strip() for line in lines if re.match(SEASON, line))
    else:
        raise AssertionError('%d containers in %s' % (len(containers), response.url))

def has_weather(response):
    return all([
        response,
        'CommonSpot Error' not in response.text,
        'Page In-Progress' not in response.text,
    ])
