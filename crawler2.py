import requests as req
from bs4 import BeautifulSoup as BS

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

names = []
tds = soup.find_all("td")
for td in tds:
    if len(td.find_all("a")) == 0:
        continue
    
    names.append(td.get_text(strip=True))
#    print(td.get_text(strip=True))
#    print(td.string)
#    for s in td.strings:
#        print(s)
#    for s in td.stripped_strings:
#        print(s)

prices = []
for td in tds:
    if "class" in td.attrs:
        if "sale" in td.attrs["class"]:
            prices.append(td.get_text(strip=True))


#print(names)
#print(prices)


names = []
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select("td.sale"):
    prices.append(td.get_text(strip=True))

print(names)
print(prices)
