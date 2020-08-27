import urllib3
import certifi


class IFTTT:

    __WEBSITE = 'https://maker.ifttt.com/trigger/{}/with/key/'

    def __init__(self, key):
        self.__WEBSITE += key
        self.__http = urllib3.PoolManager(ca_certs=certifi.where())

    def execute(self, event):
        return self.__http.request('GET', self.__WEBSITE.format(event))
