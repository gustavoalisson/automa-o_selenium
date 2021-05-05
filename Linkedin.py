import time
import selectors
import requests
from linkedin_selectors import selectors
from Selenium_Utilities.SeleniumUtilities import SeleniumUtilities

class Linkedin:
    __slots__ = 'robot'

    def __init__(self):
        self.robot = SeleniumUtilities()

    def select_url(self, url):
        self.robot.open_chrome(r'C:\Users\Alisson\Desktop\pasta_teste')
        self.robot.browser.get(url)
        
    def insert_user(self):
        click_enter = selectors['SELECTOR']
        self.robot.click(click_enter['BUTTONS']['TO_ENTER'])
        time.sleep(3)
        self.robot.insert_text('#username','gustavoalisson112@gmail.com')

    def insert_passaword(self):
        click_input_password = selectors['SELECTOR']
        self.robot.click(click_input_password['INPUTS']['INPUT_PASSWORD'])
        self.robot.insert_text('#password', 'Teste123')

    def login(self, COUNTER=1, LIMITER=3):
        enter_login = selectors['SELECTOR']
        if(COUNTER >= LIMITER):
            return 'ERRO'

        self.insert_user()
        time.sleep(3)
        self.insert_passaword()

        return self.robot.click(enter_login['BUTTONS']['ENTER_LOGIN'])

    # BAIXA O ARQUIVO POR REQUISIÇÃO E GRAVA EM UM DIRETÓRIO ESPECÍFICO
    def download_file_by_request(self,url, directory): 
        self.robot.browser.get('https://www.whatsapp.com/download/')
        request =  requests.get(url)
    
        if request.status_code == requests.codes.OK:
            with open(directory, 'wb') as new_file:
                for parte in request.iter_content(chunk_size=256):
                    new_file.write(parte)
        else:
            request.raise_for_status()    
                         
linkedin = Linkedin()
linkedin.select_url('https://www.linkedin.com/signup/cold-join')
time.sleep(3)
linkedin.login()
#linkedin.robot.intercepte(linkedin.download_file_by_request)
linkedin.download_file_by_request('https://web.whatsapp.com/desktop/windows/release/x64/WhatsAppSetup.exe', r'C:\Users\Alisson\Desktop\pasta_teste\WhatsAppSetup.exe' )

