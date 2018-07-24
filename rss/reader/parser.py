import xml.etree.ElementTree as ET

import urllib.request

lien = urllib.request.urlopen('https://hackaday.com/blog/feed/')
tree = ET.parse(lien)
root = tree.getroot()

for i in root.getchildren()[0]:
    if i.tag == 'item':
        for y in i.getchildren():
            print(y.tag , y.text)