import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd

url = "https://www.zingat.com/satilik-daire"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
pages = len(soup.find_all("ul", attrs={"class": "zng-pagination-items"})[0].find_all("li")) - 2

# toplam sayfa sayısı
a = soup.find("span", attrs={"class": "zng-pagination-link-text zng-pagination-mobile-visible"}).text.split("/")[1]


total = 0

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Location', 'Price']
    thewriter.writerow(header)

    for pageNumber in range(1, pages + 1):
        pageRequest = requests.get("https://www.zingat.com/satilik-daire?page=" + str(pageNumber))
        pageSource = BeautifulSoup(pageRequest.content, "html.parser")
        houses = pageSource.find("section", attrs={"class": "zcard-container x3"}).ul.find_all("li")
        for house in houses:
            name = house.find("div", attrs={"class": "zlc-title"}).text
            location = house.find("div", attrs={"class": "zlc-location"}).img.text.split(",")
            price = house.find("div", attrs={"class": "feature-item feature-price"}).text
            total += 1
            print(name, location, price, sep="\n")
            print("-" * 60)
            info = [name, location, price]
            thewriter.writerow(info)

print("Total {} house found.".format(total))

df=pd.read_csv("housing.csv")
print(df)