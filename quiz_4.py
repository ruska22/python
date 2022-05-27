from typing import Any

import requests
from bs4 import BeautifulSoup
file = open("music.csv", "w")
file.write('name'+','+'available'+'\n')

url = 'https://www.sheetmusicplus.com/'
resp = requests.get(url)
print(resp.headers)
content = resp.text
soup = BeautifulSoup(content, 'html.parser')
div = soup.find('div', class_='productList')
print(div)
notes = div.find_all('article')
for note in notes:
   cartItem = note.find('div', class_='visible-sm visible-xs')
   note_name = cartItem.a.text
   available = note.find('div', class_='right')
   right = note_name.b.text
   print(note_name)
   file.write(note_name + ',' + available + '\n')

