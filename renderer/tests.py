from django.test import TestCase, LiveServerTestCase
from processor.models import Docs, Version
from selenium import webdriver

class FunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        docs = Docs(owner='sulami', name='dotfiles')
        docs.save()
        ver = Version(name='master', content='')
        ver.save()
        docs.versions.add(ver)
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        for doc in Docs.objects.all():
            doc.delete()
        for ver in Version.objects.all():
            ver.delete()

    def test_site_replies(self):
        self.browser.get('http:localhost:8081')
        self.browser.implicitly_wait(3)
        self.assertIn('Django', self.browser.title)

    def test_open_repo(self):
        self.browser.get('http:localhost:8081/sulami/dotfiles/')
        self.browser.implicitly_wait(3)
        self.assertEqual('sulami/dotfiles', self.browser.title)

    def test_open_version(self):
        self.browser.get('http:localhost:8081/sulami/dotfiles/master/')
        self.browser.implicitly_wait(3)
        self.assertEqual('sulami/dotfiles/master', self.browser.title)

    def test_non_existent_repo(self):
        self.browser.get('http:localhost:8081/sulami/foobar/')
        self.browser.implicitly_wait(3)
        self.assertEqual('Not Found', self.browser.title)

    def test_non_existent_repo_version(self):
        self.browser.get('http:localhost:8081/sulami/foobar/master/')
        self.browser.implicitly_wait(3)
        self.assertEqual('Not Found', self.browser.title)

    def test_non_existent_version(self):
        self.browser.get('http:localhost:8081/sulami/dotfiles/foobar/')
        self.browser.implicitly_wait(3)
        self.assertEqual('Not Found', self.browser.title)

