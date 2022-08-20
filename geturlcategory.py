from bs4 import BeautifulSoup as bs
import lxml

#https://dubai.dubizzle.com/
class GetUrlCategory:
    def __init__(self,source_page):
        self.__source_page = source_page
        self.__bs = bs
        self.__url = 'https://dubai.dubizzle.com'
        self.__ul = None

    def get_list_category(self):
        soup = self.__bs(self.__source_page,'lxml')
        self.__ul = soup.find('ul',{'data-header-id':'list'})
        #list_url_category = soup.find_all('li',{'class':'dubizzle_menu_item '})
        dict_url_category = {li.find('a').text.replace('\n','').strip().lower():li.find('a')['href'] for li in self.__ul.find_all('li',{'class':'dubizzle_menu_item'})}
        print(dict_url_category)
        return dict_url_category

    def get_ul(self):
        return self.__ul