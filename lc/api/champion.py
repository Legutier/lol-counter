from api.utils import soup_request
from bs4 import BeautifulSoup

class Champion:
    """
    Champion API useful for scrapping needed data in 'LOL data'.
    """
    def __init__(self, champion):
        self.champion = champion
        self.champion_aux = champion.lower().strip().replace(" ", "-")
        self.counter_soup = soup_request("http://www.lolcounter.com/champions/"+self.champion_aux)

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
        weaklings = self.counter_soup.find(class_='strong-block')
        weaklings = weaklings.find_all(class_='champ-block')
        weak_list = [weakling.find(class_='name').get_text() for weakling in weaklings]
        return weak_list

    def get_guides(self):
        guide_soup = soup_request("https://www.mobafire.com/league-of-legends/"+self.champion_aux+"-guide")
        guide_soup = guide_soup.find(class_='browse-list').find_all(class_='browse-list__item')
        guide_list = [guide.get_text().strip().strip('\t').split('\n') for guide in guide_soup]
        for i in guide_list:
            print(i)
        return guide_list
