from bs4 import BeautifulSoup as bs
import lxml

class GetSubCategory:
    def __init__(self,geturlcategory):
        self.__dict_category = geturlcategory.get_list_category()
        self.__ul = geturlcategory.get_ul()
        self.__dict_subcategorys = None

#dubizzle_menu_dropdown_item 
    def __dict_subcategory(self,category):
        self.__dict_subcategorys = {li.find('a').text.replace('\n','').strip().lower() : li.find('a')['href']   for li in self.__ul.find_all('li',{'class':'dubizzle_menu_dropdown_item'}) if category in li.find('a')['href']}
        #print(self.__dict_subcategory)


    def get_subcategory(self,category):
        if category.lower() in self.__dict_category.keys():
            self.__dict_subcategory(self.__dict_category[category.lower()])

    def get_name_subcategory(self):
        for name in self.__dict_subcategorys:
            print(name)

    def choice_subcategory(self,choice):
        if choice.lower() in self.__dict_subcategorys.keys():
            print(self.__dict_subcategorys[choice.lower()])
            return self.__dict_subcategorys[choice.lower()]

    
    