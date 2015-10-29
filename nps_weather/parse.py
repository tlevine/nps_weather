import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)
    options = html.xpath('//select[@name="alphacode"]/optgroup/option')
    print(options)

def weather(response):
    html = lxml.html.fromstring(response.content)
