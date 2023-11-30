import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class SeleniumTrial():
    def __init__(self):
        #os.environ['PATH'] += '/usr/local/bin/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(time_to_wait=10.0) #Call one time per session
   
        self.driver.get("http://www.example.com")
        
        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), 'Example Domain')
        ) 
        
        #check to make sure chrome version and driver versions match
        #self.driver.capabilities
    
    def find_paragraph(self):
        elem = self.driver.find_element(By.TAG_NAME, "p")
        return elem.text



