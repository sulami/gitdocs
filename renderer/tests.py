from django.test import TestCase, LiveServerTestCase
from selenium import webdriver

class FunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_sitereplies(self):
        self.browser.get('http:localhost:8081')
        self.browser.implicitly_wait(3)
        self.assertIn('Django', self.browser.title)

