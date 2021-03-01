import logging
import time
import os
from common_tools.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_tools.project_dir import screenshot_dir,log_dir

class BasePage():

    def __init__(self,driver):
        self.driver = driver

    def wait_elemet_presences(self,loc,time=10,poll_frequency=0.2,doc=""):
        try:
            WebDriverWait(self.driver,time,poll_frequency).until(EC.presence_of_element_located(*loc))
            logger().info(f"元素{loc}存在")
        except Exception as e:
            logging.exception(f"元素{loc}不存在")
            self.driver.s_screenshot(doc)

    def s_screenshot(self,doc=""):
        logger().info(f"截图成功")
        file_name = os.path.join(screenshot_dir , f"{doc}" + time.strftime("%Y%m%d%H%M%S",time.localtime()) + ".png")
        self.driver.save_screenshot(file_name)

    def element_click(self,loc,doc=""):
        try:
            self.g_elemet(*loc).click()
            logger().info(f"查找元素{loc}成功")
            return self.driver.find_element(*loc)
        except Exception as e:
            logger().exception(f"点击元素{loc}失败")
            self.driver.s_screenshot(doc)

    def element_send_key(self,loc,key,doc=""):
        try:
            self.g_elemet(*loc).send_keys(key)
            logger().info(f"元素{loc}传值{key}成功")
            logger().info()
            return self.driver.find_element(*loc)
        except Exception as e:
            logger().exception(f"元素{loc}传值{key}失败")
            self.driver.s_screenshot(doc)

    def get_element_text(self,loc,doc=""):
        try:
            self.g_elemet(*loc).text()
            logger().info(f"元素{loc}文本打印成功")
            logger().info()
            return self.driver.find_element(*loc)
        except Exception as e:
            logger().exception(f"元素{loc}文本打印失败")
            self.driver.s_screenshot(doc)

    def g_url(self,url,doc=""):
        try:
            self.driver.get(url)
            logger().info(f"网址{url}打开成功")
            logger().info()
        except Exception as e:
            logger().exception(f"网址{url}打开失败")
            self.driver.s_screenshot(doc)

    def g_elemet(self,loc,doc=""):
        try:
            logger().info(f"元素{loc}查找成功")
            logger().info()
            return self.driver.get_element(*loc)
        except Exception as e:
            logger().exception(f"元素{loc}查找失败")
            self.driver.s_screenshot(doc)

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # driver.find_element()
    # driver.save_screenshot()
    BasePage(driver).s_screenshot("登录模块_登录功能")
    driver.quit()

