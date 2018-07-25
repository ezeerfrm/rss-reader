from .parser import Recup_rss

import sys
def recup(lien):

    test = Recup_rss(lien)
    print(str(test.liste_articles).encode(sys.stdout.encoding, errors='replace'))