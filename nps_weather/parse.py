import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)

def weather(response):
    html = lxml.html.fromstring(response.content)
