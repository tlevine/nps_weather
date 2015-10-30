import sys
import os
import argparse

from .main import nps_weather

def file(x):
    os.makedirs(x, exist_ok = True)
    return x

a = argparse.ArgumentParser('Download NPS weather information')
a.add_argument('--output', '-o', type = argparse.FileType('w'),
               default = sys.stdout)

HEADER = '''
<style>a.p { margin-left: 0.5em; background-color: grey; }</style>
<h1>Weather in United States National Parks</h1>
<p>
  These are typical weather conditions for different United States national
  parks, each taken from the park's particular weather webpage. I used the
  <a href="https://pypi.python.org/pypi/nps_weather">nps_weather package</a>
  to generate this file.
</p>
'''

PARK_TEMPLATE = '''<h2 id="%(id)s">%(name)s<a class="p" href="#%(id)s">&#182 </a></h2>
%(weather)s
<p><a href="%(url)s">Source</a></p>
'''

def cli():
    fp = a.parse_args().output
    fp.write(HEADER)
    for park in nps_weather():
        if 'weather' in park:
            park['weather'] = '<p>' + park['weather'].replace('\n\n', '</p><p>') + '</p>'
            fp.write(PARK_TEMPLATE % park)
