import unittest
import smoke
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class loginlobby(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://sta-kiv-gt2-setup01-spp-01.nix.cydmodule.com:8080/admin/tester.jsp")

    def testlobby(cls):
        username=self.driver.find_element_by_css_selector("input[name=login]")
        passw=self.driver.find_element_by_name("password")

        username.send_keys("manager")
        passw.send_keys("manager")

        self.driver.find_element_by_css_selector("input[type=submit]").click()

    def findGame(self):
        game =self.driver.find_element_by_partial_link_text('wildwild').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('undefined').click()
        sound = self.driver.find_element_by_id('soundSettingsButton')
        sound.click()



    def tearDown(self):
        self.driver.quit()
