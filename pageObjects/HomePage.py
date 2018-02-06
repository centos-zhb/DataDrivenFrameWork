# encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class HomePage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()

    def addressLink(self):
        try:
            locateType,locatorExpression = self.parseCF.getOptionValue("163mail_homePage","homePage.addressbook").split(">")
            # 获取登录成功页面的通讯录页面元素，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e