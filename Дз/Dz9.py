from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.oschadbank.ua/currency-rate")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="heading-block-currency-rate__table-txt body-regular")
    res = soup_list[9]
    asd = float(res.text)
    print("1 USD -",float(res.text),"UAH")
    # print(type(res.text))
    konv = float(input("Конвертор из UAH в USD-"))
    delit = konv / asd
    print(delit)
