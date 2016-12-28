#coding: utf8
from requests import get
import json
import datetime

def GetWeatherInfo(appid, city):
	openweathermap = 'http://api.openweathermap.org/data/2.5/weather?q='
	weatherInfo = get(openweathermap + city + appid).json()
	return weatherInfo

def GetWeatherIcon(weatherInfo):
	iconId = weatherInfo['weather'][0]['icon']
	icon = get("http://openweathermap.org/img/w/"+iconId+".png")
	return icon

def GetWeatherIconLink(weatherInfo):
	iconId = weatherInfo['weather'][0]['icon']
	return "http://openweathermap.org/img/w/"+iconId+".png"

def GetDataDateTime(weatherInfo):
	dataTime = datetime.datetime.fromtimestamp(weatherInfo['dt'])
	return dataTime

def GetSunriseDateTime(weatherInfo):
	sunrise = datetime.datetime.fromtimestamp(weatherInfo['sys']['sunrise'])
	return sunrise

def GetSunsetDateTime(weatherInfo):
	sunset = datetime.datetime.fromtimestamp(weatherInfo['sys']['sunset'])
	return sunset

def GetWeatherDescription(weatherInfo):
	return (weatherInfo['weather'][0]['main'],weatherInfo['weather'][0]['description'])

def GetTemperatureInCelsius(weatherInfo):
	return (weatherInfo['main']['temp']-273.15)

def GetHumidity(weatherInfo):
	return weatherInfo['main']['humidity']

def GetWindSpeed(weatherInfo):
	return 3.6*weatherInfo['wind']['speed']

def GetWindDirection(weatherInfo):
	dir_v = weatherInfo['wind']['deg']
	if dir_v > 348.75 and dir_v <= 11.25:
		direction = 'N'
	elif dir_v > 11.25 and dir_v <= 33.75:
		direction = 'NNE'
	elif dir_v > 33.75 and dir_v <= 56.25:
		direction = 'NE'
	elif dir_v > 56.25 and dir_v <= 78.75:
		direction = 'ENE'
	elif dir_v > 78.75 and dir_v <= 101.25:
		direction = 'E'
	elif dir_v > 101.25 and dir_v <= 123.75:
		direction = 'ESE'
	elif dir_v > 123.75 and dir_v <= 146.25:
		direction = 'SE'
	elif dir_v > 146.25 and dir_v <= 168.75:
		direction = 'SSE'
	elif dir_v > 168.75 and dir_v <= 191.25:
		direction = 'S'
	elif dir_v > 191.25 and dir_v <= 213.75:
		direction = 'SSW'
	elif dir_v > 213.75 and dir_v <= 236.25:
		direction = 'SW'
	elif dir_v > 236.25 and dir_v <= 258.75:
		direction = 'WSW'
	elif dir_v > 258.75 and dir_v <= 281.25:
		direction = 'W'
	elif dir_v > 281.25 and dir_v <= 303.75:
		direction = 'WNW'
	elif dir_v > 303.75 and dir_v <= 326.25:
		direction = 'NW'
	else:
		direction = 'NNW'
	return direction

if __name__ == '__main__':
	city = 'Pissy-Poville'
	with open('../openweathermap.appid','r') as f:
		appid = f.read()
		appid = appid[:-1]

	weather = GetWeatherInfo(appid,city)

	print(GetDataDateTime(weather))
	print(GetSunriseDateTime(weather))
	print(GetSunsetDateTime(weather))
	print(GetWeatherDescription(weather))
	print(GetTemperatureInCelsius(weather))
	print(GetWeatherIconLink(weather))
	print(GetHumidity(weather))
	print(GetWindSpeed(weather))
	print(GetWindDirection(weather))	
