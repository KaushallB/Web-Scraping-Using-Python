import requests
from bs4 import BeautifulSoup

website=requests.get('https://merojob.com/')
soup=BeautifulSoup(website.content,'html.parser')


with open('links.txt','w') as f:
    for link in soup.find_all('a'):
        links=link.get('href')
        if links:
            f.write(links + '\n')

with open('images.txt','w') as f:  
    img=soup.find_all('img')
    for tag in img:
        src=tag.get('src')
        if src:
            f.write(src + '\n')
  