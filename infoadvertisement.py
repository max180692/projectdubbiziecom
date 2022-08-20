from bs4 import BeautifulSoup as bs
import lxml

class InfoCard:
    def __init__(self,connect):
        self.__connect = connect
        self.__soup = None
        self.__content = None

    def __soup_content(self):
        self.__soup = bs(self.__content,'lxml')

    def get_content(self,url):
        self.__content = self.__connect.get_sourcepage(url)
        self.__soup_content()

    def get_title(self):
        title = self.__soup.find('h1')
        return title

