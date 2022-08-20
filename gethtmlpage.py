from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent



class GetHtmlPage:
    def __init__(self):
        self.__options = webdriver.ChromeOptions()
        self.__ua = UserAgent()
        self.__userAgent = None
    
    def __setpropertise(self):
        self.__userAgent = self.__ua.random
        print(self.__userAgent)
        self.__options.add_argument("window-size=1280,800")
        self.__options.add_argument('--headless')
        self.__options.add_argument('--no-sandbox')
        self.__options.add_argument('--disable-dev-shm-usage')
        self.__options.add_argument('--disable-blink-features=AutomationControlled')
        self.__options.add_argument(f'user-agent={self.__userAgent}')

    def get_sourcepage(self,url):
        self.__setpropertise()
        CROMEPATH = 'selen\chromedriver.exe'
        driver = webdriver.Chrome(CROMEPATH,options=self.__options)
        driver.get(url)
        source_page = driver.page_source
        driver.quit()
        return source_page