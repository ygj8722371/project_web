from selenium.webdriver.common.by import By

class Login_page():

    username = By.ID,"user_name"
    password = By.ID,"user_password"
    login_button = By.XPATH,'//button[@class="btn"]'
    username_empty_message = By.XPATH,'//label[@for="user_name"]'
    password_empty_message = By.XPATH, '//label[@for="user_password"]'
    main_page_username = By.XPATH,'//UL[@class="list-inline"]/li/a'
    username_password_dismatch = By.XPATH,'//div[@class="alert alert-error"]'