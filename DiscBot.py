import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pickle
#import chromedriver_binary  # Adds chromedriver binary to path

#driver = webdriver.Chrome()

#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

driver = webdriver.Chrome()
driver.get("https://discord.com/channels/260161878725099521/398746104738349056")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


#element = driver.find_element_by_tag_name

#element = driver.find_elements_by_css_selector 

print('a')


element = driver.find_element_by_xpath("//*[@id='app-mount']/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input")


#element = driver.find_elements_by_xpath("//input[@name='email']")

