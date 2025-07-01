import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #скрол
    browser.execute_script("window.scrollBy(0, 150);")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()

    input4 = browser.find_element(By.CSS_SELECTOR, "button")
    input4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()