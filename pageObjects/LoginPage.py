# encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemSection("163mail_login")
        print self.loginOptions

    def switchToFrame(self):
        try:
            locatorExpression = self.loginOptions["loginPage.frame".lower()].split(">")[1]
            self.driver.switch_to.frame(locatorExpression)
        except Exception,e:
            raise e

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
        except Exception,e:
            raise e

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            # 获取登录页面的用户输入框页面对象，并返回调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def passwordObj(self):
        try:
            # 从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def buttonObj(self):
        try:
            # 从定位表达式配置文件中读取定位登录按钮的定位方式和表达式
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e