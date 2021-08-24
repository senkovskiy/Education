import os
import pathlib
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get(file_uri("counter.html"))
#print(driver.title)

class WebpageTests(unittest.TestCase): 
    
    def test_title(self):
        driver.get(file_uri("counter.html"))
        print(driver.title)
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))

        increase = driver.find_element_by_id('increase')
        for i in range(100):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, '100')

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id('decrease')
        for i in range(100):
            decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, '-100')

if __name__ == "__main__":
    unittest.main()