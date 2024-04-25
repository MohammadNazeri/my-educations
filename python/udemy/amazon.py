import requests
import lxml
from bs4 import BeautifulSoup

header = {
    "Connection": "keep-alive",
    "upgrade-insecure-requests":"1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


url = "https://www.amazon.ca/dp/B07R6XYN5Q/ref=twister_B0CGWW4W1X?_encoding=UTF8&th=1"

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price = price.split("$")[1]
print(f"cookware set:", price)
#------------------------------------------------------------------
url = "https://www.amazon.ca/gp/product/B09N93L2RQ/ref=ewc_pr_img_1?smid=A2MVL5OZYL2KXQ&psc=1"

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")

#print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price = price.split("$")[1]
print(f"office desk:", price)

