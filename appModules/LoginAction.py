# encoding=utf-8
from pageObjects.LoginPage import LoginPage
import time

class LoginAction(object):
    def __init__(self):
        print ".................login................."

    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            # 将当前焦点切换到登录模块的frame中，以便能进行后续的登录操作
            login.switchToFrame()
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.buttonObj().click()
            time.sleep(3)
            # 切回到默认窗体
            login.switchToDefaultFrame()
        except Exception,e:
            raise e