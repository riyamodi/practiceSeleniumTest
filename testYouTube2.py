import unittest
from selenium import webdriver

class Selenium2OnSauce(unittest.TestCase):
	def setUp(self):
		caps = webdriver.DesiredCapabilities.CHROME
		caps['platform'] = "Windows 7"
		caps['version'] = "34"
		caps['name'] = "Practice Selenium Test YouTube"
		self.driver = webdriver.Remote(
			desired_capabilities = caps,
			#ENTER USERNAME AND ACCESS STRING IN THE LINE BELOW
			command_executor = "http://username-string:access-key-string@ondemand.saucelabs.com:80/wd/hub"
		)
		
		#sets a timeout to wait for an element to be found or for a command to complete
		self.driver.implicitly_wait(30)
	
	def testApp(self):
		self.driver.get('http://youtube.com')
		self.assertTrue("YouTube" in self.driver.title)
		
		# logo = self.driver.find_element_by_id('logo')
		# self.assertTrue(logo.isDisplayed())
	
		searchField = self.driver.find_element_by_name('search_query')
		searchField.send_keys('Harry Potter')
		self.driver.find_element_by_id('search-btn').click()
		self.assertTrue(self.driver.current_url.endswith("results?search_query=Harry+Potter"))
	
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
    unittest.main()