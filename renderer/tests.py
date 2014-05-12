from django.test import TestCase, LiveServerTestCase
from selenium import webdriver

class FunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_site_replies(self):
        self.browser.get('http:localhost:8081')
        self.browser.implicitly_wait(3)
        self.assertIn('Django', self.browser.title)

    def test_open_repo(self):
        self.browser.get('http:localhost:8081/sulami/dotfiles/')
        self.browser.implicitly_wait(3)
        self.assertNotEqual('sulami/dotfiles', self.browser.title)

    def test_open_version(self):
        self.browser.get('http:localhost:8081/sulami/dotfiles/master/')
        self.browser.implicitly_wait(3)
        self.assertNotEqual('sulami/dotfiles/master', self.browser.title)

