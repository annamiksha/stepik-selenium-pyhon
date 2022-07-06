import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_fname = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    input_lname = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    input_email = browser.find_element(By.XPATH, '//input[@name="email"]')
    button_file = browser.find_element(By.XPATH, '//input[@id="file"]')

    input_fname.send_keys('Name')
    input_lname.send_keys('LastName')
    input_email.send_keys('example@gmail.com')
    button_file.send_keys(file_path)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()
