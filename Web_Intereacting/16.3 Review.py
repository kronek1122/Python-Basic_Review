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

title = profile_page.soup.select('title')
print(title)

login_page = browser.get(url)
print(login_page.soup.select('title'))


form = login_html.select('form')[0]
form.select('input')[0]['value']='jowisz'
form.select('input')[1]['value']='ThunderDude'
error_page = browser.submit(form, login_page.url)

if error_page.soup.text.find("Wrong username or password!") != -1:
    print("Login failed.")
else:
    print("Log in")
