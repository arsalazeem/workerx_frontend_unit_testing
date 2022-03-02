import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest

loginscreen={
    "email":'//input[@id="email"]',
    "password":'//input[@id="password"]',
    "login_button":"//button[contains(text(), 'Log In')]"
}

def start():
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver
    except Exception as e:
        print(e)
        quit()

class TestStringMethods(unittest.TestCase):

    def test_login(self):
        driver = start()
        driver.implicitly_wait(30)
        driver.get("https://stagingadmin.workerx.co/")
        driver.find_element(By.XPATH,loginscreen["email"]).send_keys("arsal.azeem@vizteck.com")
        driver.find_element(By.XPATH, loginscreen["password"]).send_keys("12345678")
        driver.find_element(By.XPATH, loginscreen["login_button"]).click()
        print(driver.title)
        time.sleep(2)
        self.assertTrue('WorkerX Business',driver.title)
        driver.quit()



if __name__ == '__main__':
    unittest.main()

