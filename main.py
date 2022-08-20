from gethtmlpage import GetHtmlPage
from geturlcategory import GetUrlCategory
from geturlcity import GetUrlCity
from geturlsubcategory import GetSubCategory
from listadvertisement import ListAdvertisement
from infoadvertisement import InfoCard

def main():
    url = 'https://dubai.dubizzle.com/'
    gethtml = GetHtmlPage()
    source_page = gethtml.get_sourcepage(url)
    #print(source_page)
    getcity = GetUrlCity()
    getcity.get_list_city(source_page)
    url_city = getcity.get_url_city('Sharjah')
    get_category = GetUrlCategory(source_page)
    get_sub_category = GetSubCategory(get_category)
    get_sub_category.get_subcategory('Mobiles & Tablets')
    get_sub_category.get_name_subcategory()
    url_subcategory = get_sub_category.choice_subcategory('Mobile Phone & Tablet Accessories')
    new_url = url_city + url_subcategory
    print(new_url)
    list_advs = ListAdvertisement(gethtml,new_url,url_city)
    list_ad = list_advs.get_list_adv()
    infocard = InfoCard(gethtml)
    i = 0
    for l in list_ad:
        
        infocard.get_content(l)
        print(i)
        print(infocard.get_title())
        print(l)
        i +=1

    

if __name__ == '__main__':
    main()