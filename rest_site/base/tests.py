from django.test import TestCase
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class BasicLiveTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(BasicLiveTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(BasicLiveTestCase, self).tearDown()

    def test_home_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, reverse('home')))
        self.assertIn("REST", self.selenium.title)
