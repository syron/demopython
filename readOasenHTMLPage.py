import urllib.request
import requests
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from collections import namedtuple
import time

headers = {
    'Accept': 'application/json',
}
url = "https://eurest.mashie.com/public/menu/motorkringlan/a7b70b36?country=se"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
data = soup.script.get_text()

data = data.lstrip()
data = data.replace('var weekData = ', '')
data = data.replace('ö', 'ö')
data = data.replace('new Date(1511737200000)', '"new Date(1511737200000)"')
data = data.replace('new Date(1511823600000)', '"new Date(1511823600000)"')
data = data.replace('new Date(1511910000000)', '"new Date(1511910000000)"')
data = data.replace('new Date(1511996400000)', '"new Date(1511996400000)"')
data = data.replace('new Date(1512082800000)', '"new Date(1512082800000)"')


json = json.loads(data)
#print (json)

numberOfDays = len(json["Weeks"][0]["Days"])
numberOfAlternatives = len(json["Weeks"][0]["Days"][0]["DayMenus"])

def getMenu():
    WeekMenu = namedtuple('WeekMenu', ['Menualternative', 'Menuname'])
    _menu = []

    for i in range(0, numberOfDays):
        for j in range(0, numberOfAlternatives):
            _menu.append(WeekMenu(json["Weeks"][0]["Days"][i]["DayMenus"][j]["DayMenuName"],
                                  json["Weeks"][0]["Days"][i]["DayMenus"][j]["MenuAlternativeName"]))
    #print (_menu)
    return _menu
getMenu()
