import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)
    options = html.xpath('//select[@name="alphacode"]/optgroup/option')
    for option in options:
        yield {
            'id': str(option.xpath('@value')[0]),
            'name': str(option.xpath('text()')[0]),
        }

def weather(response):
    html = lxml.html.fromstring(response.content)
