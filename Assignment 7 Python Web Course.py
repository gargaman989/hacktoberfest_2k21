import json
import urllib.request, urllib.parse, urllib.error

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = 'University of Pennsylvania'

parms = dict()
parms['key'] = api_key
parms['address'] = address

url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
place_id = js["results"][0]["place_id"]
print("PLACE ID: ", place_id)

