import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pickle


#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
#    driver.add_cookie(cookie)


def chrometest():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    element = driver.find_element_by_xpath("//*[@name='q']")
    element.send_keys('asdf')

def discordlogin():
    driver = webdriver.Chrome()
    driver.get("https://discord.com/login")
    element = driver.find_element_by_xpath("//*[@name='q']")
    element.send_keys('asdf')

def runloop():

    print('Type [chrome] or [discord]')
    x = input()
    
    if x == ('chrome'):
        print('running Chrometest')
        chrometest()
    elif x == ('discord'):
        print('running discordlogin')
        discordlogin()
    else:
        runloop()


runloop()


#element = driver.find_elements_by_xpath("//input[@name='email']")
#print('2')
#chrometest()