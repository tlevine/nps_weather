import re

import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)
    options = html.xpath('//select[@name="alphacode"]/optgroup/option')
    for option in options:
        yield {
            'id': str(option.xpath('@value')[0]),
            'name': str(option.xpath('text()')[0]),
        }

SEASON = re.compile(r'.*(winter|spring|summer|fall|autumn).*', flags = re.IGNORECASE)
def weather(response):
    html = lxml.html.fromstring(response.content)
    containers = html.xpath('id("content-main-container")')
    if len(containers) == 1:
        lines = containers[0].text_content().split('\n')
        return '\n\n'.join(line.strip() for line in lines if re.match(SEASON, line))
    else:
        raise AssertionError('%d containers in %s' % (len(containers), response.url))

def has_weather(response):
    return all([
        response,
        'CommonSpot Error' not in response.text,
        'Page In-Progress' not in response.text,
    ])
