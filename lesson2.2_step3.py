import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Считываем значения чисел
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    # Считаем сумму
    total: int = num1 + num2
    print("Сумма чисел:", total)

    #раскрываем список и жмем на варинта = total
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(total))  # ищем элемент = total

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




