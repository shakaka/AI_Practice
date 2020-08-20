# JSON
# print the weather of a location

import json, requests, sys

# compute location from cmd
if len(sys.argv)<2:
    print('usage: location')
    sys.exit()
location = ''.join(sys.argv[1:])

# download JSON data from openweathermap.org's API
rul = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' %(location)
response = requests.get(rul)
response.raise_for_status()

# load JSON data into python variable
weatherData = json.loads(response.text)

# print weather description
w = weatherData['list']
print('current weather in %s: ' %(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('tomorrow:')
print(...)
