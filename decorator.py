import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()



    def test_search_by_category(self):
        #search textbox
        self.driver.get("https://magento.com/search/gss")
        self.search_field = self.driver.find_element_by_name("keys")
        self.search_field.clear()
        self.search_field.send_keys("phones")
        self.search_field.submit()

        products= self.driver.find_elements_by_class_name("span9")
        self.assertEqual(1,len(products))

    def test_search_by_name(self):
        self.driver.get("https://magento.com/search/gss/")
        self.search_field = self.driver.find_element_by_name("keys")
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()

        products= self.driver.find_elements_by_class_name("span9")
        self.assertEqual(1,len(products))



    def tearDown(cls):
        cls.driver.quit()
