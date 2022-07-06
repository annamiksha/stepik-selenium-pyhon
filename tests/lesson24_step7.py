from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    field = browser.find_element(By.XPATH, '//input[@id="answer"]')
    field.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
