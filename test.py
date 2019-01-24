import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class GoogleSearch(unittest.TestCase):

    def setUp(self):
        executable_path = "C:\Python37-32\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path)
        self.driver.get('http://qa-test.klika-tech.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_01(self):
        driver = self.driver
        button_1 = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[7]")
        button_1.click()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()