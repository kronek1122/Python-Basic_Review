import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

pattern = '<title.*?>.*?</title.*?>'
match_result = re.search(pattern, html,re.IGNORECASE)
title = match_result.group()
title = re.sub('<.*?>',"",title) #Remove HTML tags

print(title)
