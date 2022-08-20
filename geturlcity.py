from bs4 import BeautifulSoup as bs
import lxml

#https://dubai.dubizzle.com/
class GetUrlCity:
    def __init__(self):
        self.__bs = bs
        self.__list_all_url_city = None

    def get_list_city(self,source_page):
        soup = self.__bs(source_page,'lxml')
        self.__list_all_url_city = [{'city': li.find('a').text.replace('\n','').strip(),'url': li.find('a')['href'].replace('/','').replace(':','://')} for li in soup.find_all('li',{'data-tr-event-name':'header_city_select'})]
        print(self.__list_all_url_city)

    def get_url_city(self,city):
        for dict_url_city in self.__list_all_url_city:
            if city.lower() in dict_url_city['city'].lower():
                print(dict_url_city['url'])
                return dict_url_city['url']
