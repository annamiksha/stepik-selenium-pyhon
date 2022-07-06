import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def press_submit():
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
    time.sleep(1)


def math_is_magic():
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    y = calc(x)

    input = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input.send_keys(y)
    press_submit()


try:
    browser = webdriver.Chrome()
    browser.get(link)
    press_submit()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    math_is_magic()

finally:
    time.sleep(30)
    browser.quit()
