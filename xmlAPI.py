from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = 'https://apps.des.qld.gov.au/air-quality/xml/feed.php?category=1&region=ALL'
url_result = urlopen(url)
raw_data = url_result.read()
xml_soup = soup(raw_data, 'xml')
print(xml_soup)