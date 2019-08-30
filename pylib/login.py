
from common.record_log import logger
from selenium import webdriver
from pages.loginPage import LoginPage
from robot.libraries.BuiltIn import BuiltIn
_driver = None

def open_driver(dri):
    global _driver
    logger.info('------------open browser------------')
    _driver = webdriver.Chrome()
    BuiltIn().set_global_variable('${%s}' % dri, _driver)
    return _driver


def login_cgr(user,pwd):
    login_page = LoginPage(open_driver())
    login_page.open_url()
    login_page.login(user,pwd)

def del_cookie():
    _driver.delete_all_cookies()

def close_driver():
    _driver.quit()


if __name__ == "__main__":
    pass
