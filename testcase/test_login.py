import unittest
from selenium import webdriver
from common_tools.common_data import test_environment
from page_object.login_page import Loginpage as LG
import ddt
from test_data.login_data import login_success,login_wrong,login_empty

@ddt.ddt()
class Test_login_page(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.get(test_environment)
        self.lg = LG(driver)

    def tearDown(self):
        pass

    def test_login_success(self):
        self.lg.login(login_success[0],login_success[1])
        self.assertEqual(self.lg.get_main_page_success_username(),login_success[2])

    @ddt.data(*login_wrong)
    def test_login_wrong(self):
        self.lg.login(login_wrong[0],login_wrong[1])
        self.assertIn(login_wrong[2],self.lg.get_username_password_dismatch())

    def test_login_username_empty(self):
        self.lg.login(login_empty[0],login_empty[1])
        self.assertEqual(self.lg.get_username_empty_message(), login_empty[2])

    def test_login_password_empty(self):
        self.lg.login(login_empty[0],login_empty[1])
        self.assertEqual(self.lg.get_password_empty_message(), login_empty[2])