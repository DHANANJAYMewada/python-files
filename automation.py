# # html=inspact
# # html copy xpath
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser=webdriver.Chrome()
browser.maximize_window()
sleep(2)
browser.get("https://youtube.com")
sleep(5)
element=browser.find_element("name","search_query")
search="best india foods"
for char in search:
    element.send_keys(char)
    sleep(0.4)
sleep(2)
element.send_keys(Keys.ENTER)
sleep(10)
first_short = browser.find_element("xpath", '//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div/div[1]') 
first_short.click() 
sleep(30)
while True: 
    next_btn=browser.find_element("xpath",'//*[@id="navigation-button-down"]')
    next_btn.click() 
    sleep(30)





