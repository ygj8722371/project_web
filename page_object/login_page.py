from common_tools.base_page import BasePage
from page_locator.login_locator import Login_page as LP

class Loginpage(BasePage):

    def login(self,username,password):
        self.wait_elemet_presences(LP.username)
        self.element_send_key(LP.username,username)
        self.wait_elemet_presences(LP.password)
        self.element_send_key(LP.password,password)
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

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get("http://132.232.64.151:84/dbshop/user/login")
    time.sleep(2)
    Loginpage(driver).login("yyy001","123456")
    time.sleep(2)
    driver.quit()