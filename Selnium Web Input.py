import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pickle

#Clicking Google Search button 
#driver.find_element_by_xpath("//input[@value='Google Search']").click()

#Keyword searched in the chrometest
searchtext =('Steve Wozniak')


def chrometest():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.find_element_by_xpath("//*[@name='q']").send_keys(searchtext)  

    driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)    
    time.sleep(45)

    

def discordlogin():
    driver = webdriver.Chrome()
    driver.get("https://discord.com/login")
    element = driver.find_element_by_xpath("//input[@name='email']")
   
    element.send_keys(searchtext)
    time.sleep(45)

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