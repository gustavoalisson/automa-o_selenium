# from selenium.webdriver import Chrome
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtilities:

    def __init__(self):
        self.browser = ''
        
    def open_chrome(self, local_directory):
    #ENCAMINHA O ARQUIVO PARA OUTRO DIRETÓRIO
        options = webdriver.ChromeOptions()
        self.directory = {'download.default_directory':local_directory ,'safebrowsing.enabled':'false'}
        options.add_experimental_option('prefs', self.directory)
        self.browser = webdriver.Chrome(r'C:\tools\selenium\chromedriver', chrome_options=options)
        self.browser.maximize_window()

    # ENCONTRA E VALIDA A PRESENÇA DE QUALQUER ELEMENTO
    def find(self, selector):
        wait = WebDriverWait(self.browser, 100)
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
    #REALIZA CLICK EM QUALQUER ELEMENTO 
    def click(self, selector):
        self.find(selector).click()

    #INSERE TEXTO NO CAMPO
    def insert_text(self, selector, text):
        self.find(selector).send_keys(text)

    #INTECEPTADOR
    def intercepte(self, download_file_by_request):
        self.browser.request_interceptor = download_file_by_request

    # VERIFICAR SE DOWNLOAD FINALIZOU 
    def verify_file_in_directory(self,directory, timeout): 
        seconds = 0
        wait_download = True
        while wait_download and seconds < timeout:
            time.sleep(1)
            wait_download = False

            for file in os.listdir(directory):
                if file.endswith('.crdownload'):
                    wait_download = True
                    print('=======================BAIXANDO=======================')   
            seconds += 1
        print('DOWNLOAD FINALIZADO') 
        return seconds
