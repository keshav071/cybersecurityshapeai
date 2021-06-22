import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=jaipur&appid=5d29afb5d247f286c3d92954e8ef372f')

# print(r.text)

with open('jpr_weather.txt','wb') as ww:
    ww.write(r.content)

