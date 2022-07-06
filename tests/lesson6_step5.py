import time
from selenium import webdriver
from selenium.webdriver.common.by import By

page = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(page)

    link = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link.click()

    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Ivan')

    input2 = browser.find_element_by_name('last_name')
    input2.send_keys('Petrov')

    input3 = browser.find_element_by_class_name('city')
    input3.send_keys('Smolensk')

    input4 = browser.find_element_by_id('country')
    input4.send_keys('Russia')

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()


