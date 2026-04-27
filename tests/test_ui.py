import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ConverterTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_conversion(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        # Simulate interaction here
        self.assertIn("DevOps Data Converter", driver.title)

    def tearDown(self):
        self.driver.quit()
