# encoding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from util.ParseExcel import ParseExcel
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from appModules.AddContactPersonAction import AddContactPerson
import traceback
import time
from util.Log import *

# 设置此次测试的环境编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 创建解析Excel对象
excelObj = ParseExcel()
# 将Excel数据加载到内存
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options实例中添加禁用扩展插件中设置参数项
    chrome_options.add_argument("--disable-extensions")
    # 添加屏蔽提示信息参数项
    chrome_options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    # 添加启动最大化
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome()
    driver.get("http://mail.163.com")
    time.sleep(3)
    return driver

def test163MailAddContacts():
    logging.info(u"163邮箱添加联系人数据驱动测试开始...")
    try:
        # 根据Excel文件中sheet名称获取此sheet对象
        userSheet = excelObj.getSheetByName(u"163账号")
        # 获取163账号sheet中是否执行列
        isExecuteUser = excelObj.getColumn(userSheet,account_isExecute)
        # 获取163账号sheet中的数据表列
        dataBookColumn = excelObj.getColumn(userSheet,account_databook)

        for idx,i in enumerate(isExecuteUser[1:]):
            # 循环遍历163账号表中的账号，为需要执行的账号添加联系人
            if i.value == "y":
                # 获取第i行的数据
                userRow = excelObj.getRow(userSheet,idx + 2)
                # 获取第i行中的用户名
                username = userRow[account_username - 1].value
                password = userRow[account_password - 1].value
                print username,password

                # 创建浏览器实例对象
                driver = LaunchBrowser()
                logging.info(u"启动浏览器，访问163邮箱主页")

                # 登录
                LoginAction.login(driver,username,password)
                time.sleep(3)
                try:
                    # 断言登录后跳转页面的标题是否包含"网易邮箱"
                    assert u"收 信" in driver.page_source
                    logging.info(u"用户%s登录后，断言页面关键字'收 信'成功" %username)
                except AssertionError,e:
                    logging.debug(u"用户%s登录后，断言页面关键字'收 信'失败" u"异常信息：%s" %(username,str(traceback.print_exc())))
                # 获取第i行中用户添加的联系人数据表sheet名
                dataBookName = dataBookColumn[idx + 1].value
                # 获取对应的数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)
                isExecuteData = excelObj.getColumn(dataSheet,contacts_isExecute)
                contactNum = 0  # 记录添加成功联系人个数
                isExecuteNum = 0  # 记录需要执行联系人个数
                for id,data in enumerate(isExecuteData[1:]):
                    if data.value == "y":
                        isExecuteNum += 1
                        # 获取联系人表第id+2行对象
                        rowContent = excelObj.getRow(dataSheet,id+2)
                        contactPersonName = rowContent[contacts_contactPersonName - 1].value
                        contactPersonEmail = rowContent[contacts_contactPersonEmail - 1].value
                        isStar = rowContent[contacts_isStar - 1].value
                        contactPersonPhone = rowContent[contacts_contactPersonMobile - 1].value
                        contactPersonComment = rowContent[contacts_contactPersonComment - 1].value
                        # 添加联系人成功后，断言的关键字
                        assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
                        print contactPersonName,contactPersonEmail,assertKeyWord
                        print contactPersonPhone,contactPersonComment,isStar

                        # 执行新建联系人操作
                        AddContactPerson.add(driver,
                                             contactPersonName,
                                             contactPersonEmail,
                                             isStar,
                                             contactPersonPhone,
                                             contactPersonComment)
                        time.sleep(2)
                        logging.info(u"添加联系人%s成功" %contactPersonEmail)

                        excelObj.writeCellCurrentTime(dataSheet,rowNo=id+2,colsNo=contacts_runTime)
                        try:
                            assert assertKeyWord in driver.page_source
                        except AssertionError,e:
                            # 断言失败，在联系人工作表中写入添加联系人测试失败信息
                            excelObj.writeCell(dataSheet,"faild",rowNo=id+2,colsNo=contacts_testResult,style="red")
                            logging.info(u"断言关键字'%s'失败" % assertKeyWord)
                        else:
                            # 断言成功，写入添加联系人成功信息
                            excelObj.writeCell(dataSheet,"pass",rowNo=id+2,colsNo=contacts_testResult,style="green")
                            contactNum += 1
                            logging.info(u"断言关键字'%s'成功" % assertKeyWord)
                    else:
                        logging.info(u"联系人%s被忽略执行" %contactPersonEmail)

                    print "contactNum = %s ,isExecuteNum = %s" %(contactNum,isExecuteNum)
                    if contactNum == isExecuteNum:
                        # 如果成功添加的联系人数与需要添加的联系人数相等，说明给i个人添加联系人测试用例成功，在163账号工作表中写入成功信息，否则写入失败信息
                        excelObj.writeCell(userSheet,"pass",rowNo= idx+2,colsNo=account_testResult,style="green")
                        print u"为用户 %s 添加 %d 个联系人，测试通过！" % (username,contactNum)
                    else:
                        excelObj.writeCell(userSheet, "pass", rowNo=idx + 2, colsNo=account_testResult, style="green")
                        print u"用户 %s 被设置为忽略执行！" %excelObj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username)

                    logging.info(u"为用户%s添加%d个联系人，%d个成功\n" %(username,isExecuteNum,contactNum))
                else:
                    # 获取被忽略执行的用户名
                    ignoreUserName = excelObj.getCellOfValue(userSheet,rowNo=idx+2,colsNo=account_username)
                    logging.info(u"用户%s被忽略执行\n" %ignoreUserName)
                driver,quit()
    except Exception,e:
        print u"数据驱动框架主程序发生异常，异常信息为："
        print traceback.print_exc()