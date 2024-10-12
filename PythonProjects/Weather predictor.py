import requests as request 
from urllib.request import urlopen

url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&models=bom_access_global'

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

