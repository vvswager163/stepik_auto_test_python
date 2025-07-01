import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"


#найти путь к исполняемому файлу и  задать имя файла из этой директории
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")
    input1.send_keys('Shohran')

    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']")
    input2.send_keys('Bobovozov')

    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input3.send_keys('jopa_negra@gmail.com')

    #вложить файл
    element = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    element.send_keys(file_path)

    input4 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    input4.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()