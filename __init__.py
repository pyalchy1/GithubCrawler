import requests
from bs4 import BeautifulSoup
import random


class Crawler():
    supported_types = ["repositories", "issues", "wikis"]

    def __init__(self, keywords, proxies, type=None):
        self.keywords = keywords
        self.proxies = proxies
        if type == None:
            type = self.supported_types[0]
        self.type = type

    def search(self):
        json_resp = []

        keywords = "+".join(self.keywords)

        url = "https://github.com/search?q=%s&type=%s" % (keywords, self.type)
        proxy = {"http":"http://%s" % self.random_proxy()}
        r = requests.get(url, proxies=proxy)
        soup = BeautifulSoup(r.text, 'html.parser')
        for each in soup.find_all('a', class_='v-align-middle'):
            json_resp.append({"url":"https://github.com" + str(each['href'])})

        return json_resp

    def random_proxy(self):
        return self.proxies[random.randrange(0, len(self.proxies))]
