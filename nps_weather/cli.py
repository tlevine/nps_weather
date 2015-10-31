import sys
import os
import argparse

from .main import nps_weather

def file(x):
    os.makedirs(x, exist_ok = True)
    return x

a = argparse.ArgumentParser('Download NPS weather information',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
a.add_argument('--format', '-F', choices = ('csv', 'html'),
               help = 'Output format', default = 'html')

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
    import sys, csv

    args = a.parse_args()
    if args.format == 'html':
        fp = sys.stdout
        fp.write(HEADER)
        for park in nps_weather():
            if 'weather' in park:
                park['weather'] = '<p>' + park['weather'].replace('\n\n', '</p><p>') + '</p>'
                fp.write(PARK_TEMPLATE % park)
    elif args.format == 'csv':
        w = csv.DictWriter(sys.stdout, fieldnames = ['url', 'name', 'state', 'weather'])
        w.writeheader()
        for park in nps_weather():
            del(park['id'])
            w.writerow(park)
