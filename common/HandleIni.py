# -*- coding: UTF-8 -*-
from common.FileUtil import file_utils
import configparser
class HandleIni(object):

    file_name ="config/config.ini"
    def __init__(self):
        self.data = self.loading_ini()
    '''定位ini文件'''

    def loading_ini(self):
        file_path = file_utils.location_file(self.file_name)
        file = configparser.ConfigParser()
        file.read(file_path)
        return file

    def get_content(self,key,value):
        if key and value:
            return self.data.get(key,value)
        else:
            print("你输入的参数有误")

handle_ini = HandleIni()


