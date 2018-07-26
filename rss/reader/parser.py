import xml.etree.ElementTree as ET

from urllib.request  import Request, urlopen

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
        #extract_xml = urllib.request.urlopen(self.lien, headers={'User-Agent': 'Mozilla/5.0'})
        req = Request(self.lien, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'})

        extract_xml = urlopen(req)

        self.tree = ET.parse(extract_xml)
        self.root = self.tree.getroot()

        self.parsing()
    
    def parsing(self):

        self.liste_articles = []

        for i in self.root.getchildren()[0]:

            dico_contenu = {}
            if i.tag == 'item':
                for y in i.getchildren():
                    for champs in ['title','pubDate', 'description', 'content', 'link']:
                        if champs == y.tag:
                            dico_contenu[champs]  = y.text
                self.liste_articles.append(dico_contenu)

            #atom
            # for i in root.getchildren():
            #     if 'entry' in i.tag  :
            #         for y in i.getchildren():
            #             #print(y.tag)
            #             for champs in ['title','published',  'content', 'link']:
            #                 if champs in y.tag:
            #                     print(y.text)

        
if __name__ == "__main__":
    test = Recup_rss('http://5.51.177.66/rss-bridge-master/?action=display&bridge=Twitter&u=pythonweekly&format=Mrss')
    print(test.liste_articles)