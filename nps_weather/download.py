import vlermv

get = vlermv.Vlermv.memoize('~/.nps-weather')(requests.get)
