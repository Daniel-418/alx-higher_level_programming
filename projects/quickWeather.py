#!/usr/bin/python3

import json, requests, sys

if (len(sys.argv)) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
api_key = "d77ee6a96b02d66876652f8932c6d1ee"
url = "http://api.openweathermap.org/data/3.0/forecast/onecall?q={}&cnt=3&appid={}".format(location, api_key)
response = requests.get(url)
response.raise_for_status()

print(type(response))
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
