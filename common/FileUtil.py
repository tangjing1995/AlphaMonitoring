# -*- coding: UTF-8 -*-
import os

class FileUtil(object):


    '''
        定位到项目中文件路径 从项目根目录开始
    '''
    def location_file(self,file_name):
        path = os.path.split(os.path.realpath(__file__))[0]  # 定位类目录
        file_path = os.path.abspath(os.path.join(path,'..', file_name))  # 定位到项目根目录
        if not os.path.exists(file_path):
            print("此路径不存在：" + file_path)
        return file_path






    '''
        创建文件以及文件路径
    '''
    def mkdir_path(self,file_path):
        if os.path.exists(file_path):
            return file_path
        if  file_path.find(".")==-1:
            os.makedirs(file_path)
            return file_path
        ap_dir = os.path.abspath(os.path.join(file_path, ".."))
        if not os.path.isdir(ap_dir):
            os.makedirs(ap_dir)
        open(file_path,mode="w",encoding="utf-8")
        os.remove(file_path)
        return file_path

file_utils = FileUtil()

if __name__ == '__main__':
    print(file_utils.location_file("config"))

