from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

browser.get('https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html')

btn_add_element = browser.find_element(By.ID,"addElement")
btn_add_element.click()