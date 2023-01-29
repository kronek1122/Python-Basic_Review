from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"

page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    link_adress = 'http://olympus.realpython.org' + link['href']
    print(link_adress)

    link_page = urlopen(link_adress)
    link_html = link_page.read().decode('utf-8')
    link_soup = BeautifulSoup(link_html, 'html.parser')
    print(link_soup.get_text())
