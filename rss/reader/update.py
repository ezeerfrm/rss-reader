from .parser import Recup_rss


def recup():
    print('ok')
    test = Recup_rss("http://blog.idleman.fr/feed/" )
    print(test.liste_articles)