import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

pattern_color = 'Favorite Color: .*?[\n<]'
pattern_name = 'Name: .*?[\n<]'

match_result = re.search(pattern_name,html, re.IGNORECASE)
name = match_result.group()
name = re.sub('.*?:',"",name)
print(name.strip(' \n<'))

match_result1 = re.search(pattern_color,html, re.IGNORECASE)
color = match_result1.group()
color = re.sub('.*?:',"",color)
print(color.strip(' \n<'))