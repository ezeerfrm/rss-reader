import xml.etree.ElementTree as ET

import urllib.request

# lien = urllib.request.urlopen('https://hackaday.com/blog/feed/')
# tree = ET.parse(lien)
# root = tree.getroot()

# for i in root.getchildren()[0]:
#     if i.tag == 'item':
#         for y in i.getchildren():
#             print(y.tag , y.text)

class Recup_rss:
    def __init__(self,lien):
        self.lien = lien
        extract_xml = urllib.request.urlopen(self.lien)
        self.tree = ET.parse(extract_xml)
        self.root = self.tree.getroot()

        self.parsing()
    
    def parsing(self):

        self.liste_articles = []

        for i in self.root.getchildren()[0]:

            dico_contenu = {}
            if i.tag == 'item':
                for y in i.getchildren():
                    for champs in ['title','pubDate', 'description', 'content']:
                        if champs == y.tag:
                            dico_contenu[champs]  = y.text
                self.liste_articles.append(dico_contenu)

        
if __name__ == "__main__":
    test = Recup_rss('http://sebsauvage.net/bon-android/rss.php')
    print(test.liste_articles)