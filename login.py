import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest

loginscreen = {
    "email": '//input[@id="email"]',
    "password": '//input[@id="password"]',
    "login_button": "//button[contains(text(), 'Log In')]"
}


def start():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
        driver.maximize_window()
        return driver
    except Exception as e:
        print(e)
        quit()


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.driver = start()
        self.driver.implicitly_wait(30)

    def test_login(self):
        self.driver.get("https://stagingadmin.workerx.co/")
        self.driver.find_element(By.XPATH, loginscreen["email"]).send_keys("arsal.azeem@vizteck.com")
        self.driver.find_element(By.XPATH, loginscreen["password"]).send_keys("12345678")
        self.driver.find_element(By.XPATH, loginscreen["login_button"]).click()
        print(self.driver.title)
        self.assertTrue('WorkerX Business', self.driver.title)

    def test_login_with_incorrect_password(self):
        self.driver.get("https://stagingadmin.workerx.co/")
        self.driver.find_element(By.XPATH, loginscreen["email"]).send_keys("arsal.azeem@vizteck.com")
        self.driver.find_element(By.XPATH, loginscreen["password"]).send_keys("1234567810")
        self.driver.find_element(By.XPATH, loginscreen["login_button"]).click()
        print(self.driver.title)
        self.assertTrue('WorkerX Business', self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
