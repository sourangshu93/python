import requests
import json5 
import urllib.request

#url=urllib.request.urlopen("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
#print(json5.loads(url.read()))
r=requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
print(r.json())