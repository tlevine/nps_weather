import vlermv
import requests

get = vlermv.Vlermv.memoize('~/.nps-weather')(requests.get)
