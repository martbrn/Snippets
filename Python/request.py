# EKO PARTY CTF.
# importing the requests library 
import requests 
import re

# api-endpoint 
URL = "http://paste.ubuntu.com/p/HnGHwGk4rQ/"
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 

while True:
    r = requests.get(url = URL)
    print (URL) 
    var = re.findall(r"paste.ubuntu.com/p/[a-zA-Z0-9]{10}", r.text,flags=re.MULTILINE)
    for url in var:
        r = requests.get('http://'+ url) 
        if (r.status_code != 404):
            URL = 'http://'+ url
            break
