import mechanicalsoup
import time

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/dice"

for i in range(4):
    page = browser.get(url)
    tag = page.soup.select('#result')[0]
    result = tag.text
    print(f"The result of roll is: {result}")
    print(page.soup.select('#time')[0].text)
    if i<3:
        time.sleep(10)