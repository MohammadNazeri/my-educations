# beautifulsoup is able to parse html and xml languages
import requests
from bs4 import BeautifulSoup
#import lxml 

webpage = requests.get("http://google.com")
webpage_content = webpage.text

soup = BeautifulSoup(webpage_content, "html.parser") # lxml is another option for parsing html
#print(soup)
#print(soup.prettify())
#print(soup.title)
#print(soup.title.string)
#print(soup.a)
all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)
for tag in all_anchor_tags:
	#print(tag.getText())
	print(tag.get("href"))
	
company_url = soup.select_one(selector="p a")
print(company_url)

