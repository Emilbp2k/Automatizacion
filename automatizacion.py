import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://ec2-3-87-188-193.compute-1.amazonaws.com")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()