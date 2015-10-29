import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)
#   html.xpath('//

def weather(response):
    html = lxml.html.fromstring(response.content)
