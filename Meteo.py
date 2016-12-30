#coding: utf8

from peewee import *

f = open("~/.mySQLCredentials",'r')
cr = f.readline()
f.close()
t = cr.split(',')
u = t[0]
p = t[1][:-1]

print(p)
	
db = MySQLDatabase('meteoStation',user=u,passwd=p)

class Meteo(Model):
	dataDateTime = IntegerField()
	designation = CharField()
	description = TextField()
	temperature = FloatField()
	humidity = IntegerField()
	windSpeed = FloatField()
	windDirection = CharField()
	

	class Meta:
		database = db

