import urllib.request
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = " http://py4e-data.dr-chuck.net/comments_489469.xml"
data = urllib.request.urlopen(url).read()
xml = ET.fromstring(data)
tags = xml.findall("comments/comment")

result=0
for tag in tags:
    result+=int(tag.find('count').text)
    
print(result)
