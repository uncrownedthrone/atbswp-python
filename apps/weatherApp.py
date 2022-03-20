import requests
import datetime


resp = requests.get(api_url).json()

sunrise_UTC = resp['sys']['sunrise']
sunset_UTC = resp['sys']['sunset']


def getTime(e):
    return datetime.datetime.fromtimestamp(
        e
    ).strftime('%-I:%M %p')


sunriseET = getTime(sunrise_UTC)
sunsetET = getTime(sunset_UTC)

print(f'''Good morning, Justin.
Sunrise today is {sunriseET} and
Sunset is {sunsetET}''')
