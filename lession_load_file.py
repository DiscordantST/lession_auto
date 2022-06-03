import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome() #test
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

with open("test.txt", "w") as file:
    content = file.write("automationbypython")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла


var1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
var1.send_keys('1')
var2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
var2.send_keys('2')
var3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
var3.send_keys('3')

var4 = browser.find_element(By.CSS_SELECTOR, "[id='file']")
var4.send_keys(file_path)

var5 = browser.find_element(By.TAG_NAME, 'button')
var5.click()