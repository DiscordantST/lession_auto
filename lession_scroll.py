import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
button2 = int(button.text)
button3 = str(math.log(abs(12 * math.sin(button2))))

answer = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
answer.send_keys(button3)
time.sleep(1)

check = browser.find_element(By.CSS_SELECTOR, "[id=robotCheckbox]")
check.click()

radio = browser.find_element(By.CSS_SELECTOR, "[id=robotsRule]")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()


but = browser.find_element(By.TAG_NAME, "button")
but.click()