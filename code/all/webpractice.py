from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitforload(driver):
    elem=driver.find_element_by_tag_name('html')
    count=0
    while True:
        coutn+=1
        if count>20:
            print('Timing out after 10 seconde and returning')
            return None
        time.sleep(5)
        try:
            elem==driver.find_element_by_tag_name('html')
        except StaleElementReferenceException as e:
            return
driver=webdriver.Chrome()
driver.get('http://pythonscraping.com/pages/javascript/redirectdemo1.html')
waitforload(driver)
print(driver.page_source)