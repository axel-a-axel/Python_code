import requests
import json
appid = '371cc40a486dc25ae3d0ab7f86d7ac80'
lat = '52.234322448775295'
lon = '20.979280431927965'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}'
print(url)
response = requests.get(url=url)
json_response = json.loads(response.content)
print(json_response)
