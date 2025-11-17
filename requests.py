import requests
import time

url="https://merojob.com/category/it-telecommunication"

time.sleep(5)
req=requests.get(url)

with open("data.html","w") as f:
    f.write(req.text)