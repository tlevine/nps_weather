from distutils.core import setup

setup(name='nps_weather',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Look up typical weather in United States National Park Service parks',
      url='http://dada.pink/nps_weather/',
      packages=['nps_weather'],
      install_requires = [
          'lxml>=3.3.0',
          'requests>=2.7.0',
      ],
      version='0.0.2',
      license='AGPL',
      entry_points = {'console_scripts': ['nps-weather = nps_weather.cli:cli']},
)
