from requests_html import HTMLSession

session = HTMLSession()

req=session.get('https://merojob.com/')

print(req.text)
print(req.html.links)
