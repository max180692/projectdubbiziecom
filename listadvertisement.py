from bs4 import BeautifulSoup as bs
import lxml


class ListAdvertisement:
    def __init__(self,gethtml,url,url_city):
        self.__get_html = gethtml
        self.__source_page = None
        self.__soup = None
        self.__url = url
        self.__url_city = url_city
    
    def __soup_adv(self):
        self.__soup = bs(self.__source_page,'lxml')

    def get_list_adv(self,col_number_page=None):
        if col_number_page:
            list_url_pages = self.__pagination(col_number_page)
            return [self.__list_adv(url_page) for url_page in list_url_pages]
        else:
            return self.__list_adv(self.__url)


    def __get_url_pagination(self,pages):
        self.__source_page = self.__get_html.get_sourcepage(self.__url)
        self.__soup_adv()
        
        if self.__soup.select_one('.list-listings'):
            return range(pages)
        elif self.__soup.select_one('#listings-top') or self.__soup.select_one('#results-list'):
            return range(1,pages+1)
        

    def __list_adv(self,url):
        self.__source_page = self.__get_html.get_sourcepage(url)
        self.__soup_adv()
        
        if self.__soup.select_one('.list-listings'):
            css_adv = self.__soup.select_one('.list-listings')
            list_advs = [self.__url_city + a['href']  for a in css_adv.find_all('a')]
            return list_advs
        elif self.__soup.select_one('#listings-top'):
            css_adv = self.__soup.select_one('#listings-top')
            list_advs = [self.__url_city + a['href']  for a in css_adv.find_all('a',{'class':'bWFNHV'})]
            return list_advs
        elif self.__soup.select_one('#results-list'):
            css_adv = self.__soup.select_one('#results-list')
            list_advs = [a['href']  for a in css_adv.find_all('a',{'class':'lpv-link-item'})]
            return list_advs
        
        return 'No adv'

    def __pagination(self,pages):
        return [ self.__url + '?page={}'.format(i)  for i in self.__get_url_pagination(pages)]
        
