import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

var1 = browser.find_element(By.TAG_NAME, "button")
var1.click()
alert = browser.switch_to.alert
alert.accept()
button = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
button2 = int(button.text)
button3 = str(math.log(abs(12 * math.sin(button2))))
answer = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
answer.send_keys(button3)
time.sleep(1)
button4 = browser.find_element(By.TAG_NAME, 'button')
button4.click()
browser.quit()
'''

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

var1 = browser.find_element(By.TAG_NAME, 'button')
var1.click()

var2 = browser.window_handles[1]
browser.switch_to.window(var2)
button = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
button2 = int(button.text)
button3 = str(math.log(abs(12 * math.sin(button2))))
answer = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
answer.send_keys(button3)
time.sleep(1)
button4 = browser.find_element(By.TAG_NAME, 'button')
button4.click()
browser.quit()