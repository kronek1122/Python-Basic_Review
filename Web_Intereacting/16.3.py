import mechanicalsoup

browser = mechanicalsoup.Browser()
base_url = "http://olympus.realpython.org/"
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select('form')[0]
form.select('input')[0]['value']='zeus'
form.select('input')[1]['value']='ThunderDude'

profile_page = browser.submit(form, login_page.url)

links = profile_page.soup.select('a')

for link in links:
    adress = base_url + link['href']
    text = link.text
    print(f"{text}:{adress}")