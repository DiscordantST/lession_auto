from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



class TestAbs(unittest.TestCase):
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def test_firth(self):
        touch = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        touch.send_keys('1')
        touchTwo = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        touchTwo.send_keys('1')
        touchThree = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        touchThree.send_keys('1')
        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text)
        self.browser.quit()


    def test_two(self):
        touch = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        touch.send_keys('1')
        touchTwo = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        touchTwo.send_keys('1')
        touchThree = self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        touchThree.send_keys('1')
        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

