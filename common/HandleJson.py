# -*- coding: UTF-8 -*-
import json
from common.FileUtil import file_utils


class HandleJson(object):


    '''读取json文件信息'''
    def read_json(self,file_name=None):
        if file_name==None:
            return None
        with open(file_utils.location_file(file_name),encoding='utf-8') as info:
            data = json.load(info)
        return data


    '''根据json中字段获取值'''
    def get_data_value(self,file_name,key):
        data =self.read_json(file_name=file_name)
        return data[key]

    '''根据json中字段获取值'''
    def set_data_value(self,file_name,key,key_data):
        data =self.read_json(file_name=file_name)
        data[key] = key_data
        self.write_json(data)

        return data[key]


    '''写入json信息'''
    def write_json(self,data,file_name=None):
        data_value = json.dumps(data,indent=4)
        if file_name!=None:
            with open(file_utils.location_file(file_name),"w") as info:
                info.write(data_value)

    def search_key(self, key):
        json_object = json.loads(data)
        self.result_list = []
        self.__search(json_object, key)
        return self.result_list

    def __search(self,json_object,key):
        for k in json_object:
            if k == key:
                print(json_object[k])
                # self.result_list.append(json_object[k])
            if isinstance(json_object[k], dict):
                self.__search(json_object[k], key)
                print(json_object[k])
            if isinstance(json_object[k], list):
                for item in json_object[k]:
                    if isinstance(item, dict):
                        self.__search(item, key)
        return

handle_json = HandleJson()
