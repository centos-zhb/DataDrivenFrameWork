# encoding=utf-8
from ConfigParser import ConfigParser
from config.VarConfig import pageElementLocatorPath
'''
解析存储定位页面元素得定位表达式文件，以便获取定位表达式
'''
class ParseConfigFile(object):

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemSection(self,sectionName):
        """
        获取配置文件中指定section下得所有option键值对，并以字典类型返回给调用者
        注意：
            使用self.cf.items(sectionName)此种方法获取到的配置文件中得options内容均被转换成小写
        :param sectionName:
        :return:
        """
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName,optionName):
        # 获取指定section下得指定option得值
        value = self.cf.get(sectionName,optionName)
        return value