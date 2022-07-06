import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

page = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(page)

    x = browser.find_element(By.XPATH, '//span[@id="num1"]')
    y = browser.find_element(By.XPATH, '//span[@id="num2"]')
    sum = x + y

    select = Select(browser.find_element(By.XPATH, '//select'))
    select.select_by_value(sum)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
