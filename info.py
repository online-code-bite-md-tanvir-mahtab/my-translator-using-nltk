# from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.chrome.options import Options


class Translate:

    def __init__(self,user_input):
        self.edge_path = 'demoreader/chromedriver.exe'
        self.option = Options()
        self.option.headless = True
        # self.edge_path = 'demoreader/msedgedriver.exe'
        # self.edge_path = 'demoreader/chromedriver'
        self.user_input = user_input

        self.driver = webdriver.Chrome(executable_path=self.edge_path, options=self.option)
        # self.driver.get(url=f"https://translate.google.co.uk/?tl={user_input}")
        # https://translate.google.com/?hl=english&sl=auto&tl=bn&text=hello&op=translate
        # self.driver.get(url=f"https://translate.google.com/?hl=english&tl={self.user_input}")
        self.driver.get(url=f"https://translate.google.com/?hl=english&sl=auto&tl={self.user_input}&op=translate")
        self.driver.implicitly_wait(10)

    # TODO: you need to add another mehtod how we have build on google meet for the cookie
    # TODO: please uncomment thhe find_the_pop method 

    # def find_the_pop(self):
    #     sleep(3)
    #     # pop = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[1]/div')
    #     pop = WebDriverWait(self.driver,10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[1]/div'))
    #     )
    #     print(pop.text)
    def select_the_language(self,main_text):
        self.driver.maximize_window()
        sleep(2)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/button/div[3]'))
        ).click()
        sleep(3)
        # this part is about to got to a separate function
        # this part will search the language form the search bar and press enter
        main_search_element = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[2]/input')
        main_search_element.send_keys(main_text)
        sleep(3)
        main_search_element.send_keys(Keys.ENTER)
        sleep(4)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]'))).click()
            
        sleep(3)
        search_element = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input')
        search_element.send_keys(self.user_input)
        sleep(3)
        search_element.send_keys(Keys.ENTER)

        
    # creating an method that will send the message to the google translater
    def send_the_text_to_google(self,text):
        print("=====the sending processes is started=====")
        self.driver.maximize_window()
        # now i am going to check if there is any kind of cookies in the site
        cookie = self.driver.get_cookies()
        if len(cookie) != 0:
            print("======there is cookie======")
            self.driver.delete_all_cookies()
            
            
            # after that we are sending the text to the input section
            main_text = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
            # TODO: WE ALSO  need to comment out the loop and change the word to text in the method calling
            # for word in text:

            main_text.send_keys(text)
            # TODO: YOU HAVE TO CONTROL THE SPPED IN HERE
            time = random.randint(1,5)
            sleep(time)
            
        if len(cookie) == 0:
            print("====There is no cookie======")
            
            # now i am going to triger
            # now i am going to find the element
            main_text = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
            # TODO: WE ALSO  need to comment out the loop and change the word to text in the method calling
            # for word in text:
            main_text.send_keys(text)
            # TODO: YOU HAVE TO CONTROL THE SPPED IN HERE
            time = random.randint(1,5)
            sleep(time)
        self.driver.implicitly_wait(10)
            
        
    # now i am going to get the info
    def get_the_translated_data(self):
        self.driver.implicitly_wait(3)
                                                        
        text = self.driver.find_element_by_xpath(xpath='/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]')
        # text = self.driver.find_element_by_xpath(xpath='/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[7]/div/div[1]/span[1]/span/span')
        # text = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span')
        # text = self.driver.find_element_by_xpath('//*[@id="ow236"]/div[1]')
        return text.text

    def clean_the_text(self):
        self.driver.implicitly_wait(3)
        main_text = self.driver.find_element_by_xpath(xpath='//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
        main_text.clear()


    def close_driver(self):
        self.driver.quit()





# sentences = ['hello world','hello tanvir','i hate my life']
# t = Translate("bengali")
# t.select_the_language("English")
# # t.find_the_pop()
# for text in sentences:
#     t.send_the_text_to_google(text)
#     print(t.get_the_translated_data())
#     t.clean_the_text()
# t.close_driver()
