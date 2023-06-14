import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mp_mv250"
html = requests.get(url).content
soup=BeautifulSoup(html,"html.parser")
list=soup.find('tbody',{"class":"lister-list"}).find_all("tr")
count=0
for i in list:
    count+=1
    title=i.find("td",{"class":"titleColumn"}).find("a").text
    year=i.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    rating=i.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count} - {title.ljust(50)} - {year} - {rating}")


