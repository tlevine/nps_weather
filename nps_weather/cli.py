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

HEADER = '''Weather in United States National Parks
========================================
These are typical weather conditions for different United States national
parks, each taken from the park's particular weather webpage. I used the
`nps_weather package <https://pypi.python.org/pypi/nps_weather>`_
to generate this file.

'''

PARK_TEMPLATE = '''[%(name)s](%(url)s)
----------------------------------------
%(weather)s

'''

def cli():
    fp = a.parse_args().output
    fp.write(HEADER)
    for park in nps_weather():
        if 'weather' in park:
            fp.write(PARK_TEMPLATE % park)
