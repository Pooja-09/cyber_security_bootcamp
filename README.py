import sys

import requests
from datetime import datetime

api_key = '3b62327780e83d08f2137233fed4a7c6'
location = input("Enter The City Name : ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

sys.stdout = open(" output.txt","w")
print("------------------------------------------------------")
print("Weather Stats For - {} || {}".format(location.upper(), date_time))
print("------------------------------------------------------")

print("Current Temperature Is :  {:.2f} deg C".format(temp_city))
print("Current Weather Desc :", weather_desc)
print("Current Humidity     :", hmdt, '%')
print("Current Wind Speed   :", wind_spd, 'kmph')

sys.stdout.close()



