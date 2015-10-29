import os
import argparse

from .main import nps_weather

def directory(x):
    os.makedirs(x, exist_ok = True)
    return x

a = argparse.ArgumentParser('Download NPS weather information')
a.add_argument('output-directory', type = directory)

def cli():
    output_directory = getattr(a.parse_args(), 'output-directory')
    for park in nps_weather():
        if 'weather' in park:
            fn = os.path.join(output_directory, park['id'] + '.txt')
            with open(fn, 'w') as fp:
                fp.write(park['name'] + '\n=====\n\n' + park['weather'])
