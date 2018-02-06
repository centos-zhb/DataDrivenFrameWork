# encoding=utf-8
from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time

class AddContactPerson(object):
    def __init__(self):
        print "add contact person."

    @staticmethod
    def add(driver,contactName,contactEmail,isStar,contactPhone,contactComment):
        try:
            # 创建主页实例对象
            hp = HomePage(driver)
            # 单击通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            # 创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            time.sleep(3)
            if contactName:
                # 非必填项
                apb.contactPersonName().send_keys(contactName)
                # 必填项
                apb.contactPersonEmail().send_keys(contactEmail)
                if isStar == u"是":
                    # 非必填项
                    apb.starContacts().click()
                    time.sleep(3)
                if contactPhone:
                    # 非必填项
                    contactPhone=str(contactPhone)
                    apb.contactPersonMobile().send_keys(contactPhone)
                if contactComment:
                    print contactComment
                    apb.contactPersonComment().send_keys(contactComment)
                apb.saveContacePerson().click()
                time.sleep(5)
        except Exception,e:
            # 打印堆栈信息
            print traceback.print_exc()
            raise e