import sqlite3
from bs4 import BeautifulSoup
import requests
response = requests.get("https://meteo.ua/56/cherkassyi")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="weather-detail__main-temp js-weather-detail-value")
    res = soup_list[0]
    asd = (res.text)
    print(asd)

response = requests.get("https://meteo.ua/56/cherkassyi")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="page-header-info__details")
    res = soup_list[0]
    asd1 = (res.text)
    print(asd1)

connection = sqlite3.connect("itsteps_DB.sl3", 5)
cur = connection.cursor()
# cur.execute("CREATE TABLE Cherkasi (datatime TEXT, temperature TEXT);")
cur.execute("INSERT INTO Cherkasi (datatime) VALUES (?)",(asd1,))
cur.execute("INSERT INTO Cherkasi (temperature) VALUES (?)",(asd,))
# cur.execute("ALTER TABLE ")
connection.commit()
connection.close()