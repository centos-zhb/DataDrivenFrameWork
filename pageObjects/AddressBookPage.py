# encoding=utf-8
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile

class AddressBookPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.addContactsOptions = self.parseCF.getItemSection("163mail_addContactsPage")
        print self.addContactsOptions

    def createContactPersonButton(self):
        # 获取新建联系人按钮
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.createContactsBtn".lower()].split(">")
            # 获取新建联系人的按钮页面元素，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def contactPersonName(self):
        # 获取新建联系人界面中的姓名输入框
        try:
            locateType,locatorExpression = self.addContactsOptions["addContactsPage.contactPersonName".lower()].split(">")
            # 获取新建联系人界面的姓名输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def contactPersonEmail(self):
        # 获取新建联系人界面中的电子邮件输入框
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonEmail".lower()].split(">")
            # 获取新建联系人界面的姓名输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def starContacts(self):
        # 获取新建联系人界面中的星标联系人选择框
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.starContacts".lower()].split(">")
            # 获取新建联系人界面的星标联系人复选框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def contactPersonMobile(self):
        # 获取新建联系人界面中的联系人手机号输入框
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonMobile".lower()].split(">")
            # 获取新建联系人界面的联系人手机号输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def contactPersonComment(self):
        # 获取新建联系人界面中的联系人备注信息输入框
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.contactPersonComment".lower()].split(">")
            # 获取新建联系人界面的联系人备注信息输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception,e:
            raise e

    def saveContacePerson(self):
        # 获取新建联系人界面中的保存联系人输入框
        try:
            locateType, locatorExpression = self.addContactsOptions["addContactsPage.saveContacePerson".lower()].split(">")
            # 获取新建联系人界面的保存联系人输入框页面元素，并返回给调用者
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception,e:
            raise e