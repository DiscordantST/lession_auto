from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
'''
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

browser.quit()

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
browser.quit()
'''

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
#

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button2 = browser.find_element(By.ID, 'book')

element = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
button2.click()

button = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
button2 = int(button.text)
button3 = str(math.log(abs(12 * math.sin(button2))))
answer = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
answer.send_keys(button3)
button4 = browser.find_element(By.ID, 'solve')
button4.click()
