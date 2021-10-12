import unittest
from datetime import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver import ActionChains

class Mytestslider(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver_win32_93\chromedriver.exe")

    def test_testdrag(self):

        elm = self.driver.find_element_by_xpath("//input[@value='0']")
        move = ActionChains(self.driver)
        move.click_and_hold(elm).move_by_offset(131, 0).release().perform()
        target1 = browser.find_element_by_id('range')
        print(target1.text)
        self.assertEqual("100", target1.text)
        time.sleep(5)

    def tearDown(self):
            self.browser.quit()

    if _name_ == '_main_':
        unittest.main()