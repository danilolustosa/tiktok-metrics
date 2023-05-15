from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

class Post():
    def __init__(self):
        chrome_options = Options()        
        chrome_options.add_argument('--disable-extensions')
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        #path = "C:\ChromeDrive\chromedriver.exe"
        path = "chromedriver"

        ''' Windows'''        
        #self.driver = Chrome(path, chrome_options=chrome_options)

        ''' LINUX '''
        self.driver = Chrome(path, chrome_options=chrome_options)

    def read(self, posts):
        for post in posts:
            print(post["url"])
            
            driver = self.driver        
            driver.get(post["url"])

            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'tiktok-sfaea2-SpanOtherInfos e17fzhrb2')))
            except NoSuchElementException:
                print("Erro")
        

            break