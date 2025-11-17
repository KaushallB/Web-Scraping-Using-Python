import requests
from bs4 import BeautifulSoup

website=requests.get('https://merojob.com/office-assistant-622')
soup=BeautifulSoup(website.content,'html.parser')

print(website.status_code)
#print(soup.prettify())
print(soup.title)
#print(soup.p)

tag=soup.html
print(tag.p.sting)
print(soup.body)

print(soup.find_all('p'))

class_data=soup.find("div",class_="container")
for l in class_data:
    print(l.text)
#print(class_data)

lines=soup.find_all('p')
for a in lines:
    print(a.text)

text=soup.find('div',class_='bg-white rounded-xl shadow-sm px-6 py-4 space-y-3')
line=text.find_all('p')
for b in line:
    print(b.text)
