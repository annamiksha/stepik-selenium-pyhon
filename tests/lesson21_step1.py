import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


page = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(page)

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', input)
    input.send_keys(y)

    browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    time.sleep(1)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
