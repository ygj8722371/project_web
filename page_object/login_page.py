from common_tools.base_page import BasePage
from page_locator.login_locator import Login_page as LP

class Loginpage(BasePage):

    def login(self,username,password):
        self.element_send_key(LP.username,username)
        self.element_send_key(LP.username,password)
        self.element_click(LP.login_button)

    def get_username_empty_message(self):
        self.wait_elemet_presences(LP.username_empty_message)
        return self.get_element_text(LP.username_empty_message)

    def get_password_empty_message(self):
        self.wait_elemet_presences(LP.password_empty_message)
        return self.get_element_text(LP.password_empty_message)

    def get_main_page_success_username(self):
        self.wait_elemet_presences(LP.main_page_username)
        return self.get_element_text(LP.main_page_username)

    def get_username_password_dismatch(self):
        self.wait_elemet_presences(LP.username_password_dismatch)
        return self.get_element_text(LP.username_password_dismatch)