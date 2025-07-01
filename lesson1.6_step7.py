import fake
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

link = "http://suninjuly.github.io/huge_form.html"
fake = Faker()
word = fake.job()

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #ищем все поля для ввода текста
    elements = browser.find_elements(By.TAG_NAME, "input")
    #заполняем все поля подготовленным текстом
    for element in elements:
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла