import lxml.html

def findapark(response):
    html = lxml.html.fromstring(response.content)
    print(html.xpath('//ul[@class="multiselect-container dropdown-menu"]'))

def weather(response):
    html = lxml.html.fromstring(response.content)
