from .parser import Recup_rss
from .models import Rss_a_suivre, Articles
import sys, datetime
def recup(lien_rss):
  
    test = Recup_rss(lien_rss)
    if len(test.liste_articles) > 0:

        for i in test.liste_articles:
            date_article = (i.get('pubDate', None).encode(sys.stdout.encoding, errors='replace'))
            try:
                date_article = (datetime.datetime.strptime(date_article.decode('UTF-8').replace(' GMT',' +0000')[:-6], '%a, %d %b %Y  %H:%M:%S'))
            except ValueError:
                date_article = (datetime.datetime.strptime(date_article.decode('UTF-8')[:-6], '%Y-%m-%d %H:%M'))

            lien_article = (i.get('link', None))

            origine_article = Rss_a_suivre.objects.get(lien=lien_rss)

            titre_article = i.get('title', None)

            description_article = i.get('description', 'pas de description')

            

            if description_article == None:
                description_article =  'pas de description'

            try:
                Articles.objects.get(lien = lien_article)
            except Articles.DoesNotExist:
                try:
                    Articles.objects.create( origine = origine_article,title = titre_article, pubDate = date_article , description = description_article, lien = lien_article)
                except :
                    print(description_article)

    #datetime.datetime.strptime(struc.decode('UTF-8'), '%a, %d %b %Y  %H:%M:%S +0000')
    #print(i.get('title', None))
    # if len(test.liste_articles)==0:
    #     print('mauvais scan')
    #print(str(test.liste_articles).encode(sys.stdout.encoding, errors='replace'))
