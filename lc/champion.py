import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

class Champion:
    def __init__(self, champion):
        self.champion = champion
        self.champion_aux = champion.lower().strip().replace(" ", "-")
        url= "http://www.lolcounter.com/champions/"+self.champion_aux
        req = Request(url, headers={'User-Agent' : "counter-lol"})
        respuesta = urlopen(req)
        contenido_web = respuesta.read()
        self.counter_soup = BeautifulSoup(contenido_web, "html.parser")

    def __repr__(self):
        return 'Champion(%r)' % (self.champion)

    def get_counters(self):
        """
        returns: counters list of the desired champion.
        """
        counters = self.counter_soup.find(class_='weak-block')
        counters = counters.find_all(class_="champ-block")
        counter_list = [counter.find(class_='name').get_text() for counter in counters]
        return counter_list

    def get_strongs(self):
        """
        function to get the weakest champions against champion
        """
        strong_to = self.counter_soup.find(class_='strong-block').get_text()
        print(strong_to)
        return
