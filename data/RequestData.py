# -*- coding: UTF-8 -*-
import json
from local_info import *
from common.BaseRequest import base_request
from common.HandleJson import handle_json
from common.LoggerConfig import logger
class RequestData():



    def __init__(self):
        self.handle_info={}

    '''
           登录
    '''
    def login(self,url,data):
        self.handle_info = handle_json.read_json(handler_path)
        j_data = base_request.send_request("post",url,data).json()
        logger.info(f"登录请求:{j_data}")
        self.handle_info['Handler']['companyId'] = j_data.get('data')["companyId"]
        self.handle_info['Handler']['userId'] = j_data.get('data')["userId"]
        logger.info(f"最新的handle:{ self.handle_info}")
        handle_json.write_json( self.handle_info,handler_path)

    '''
        总成功率
    '''
    def get_all_success_rate(self,url):
        data = base_request.send_request("post",url,header= self.handle_info["Handler"]).json()
        logger.info(f'总成功率:{data}')
        return data.get('data')

    '''
        总用气量
    '''
    def get_all_gas_amount(self,url):
        data = base_request.send_request("post",url, header= self.handle_info["Handler"]).json()
        logger.info(f'总用气量:{data}')
        return data.get('data')

    '''
        充值总数
    '''
    def get_all_pyment(self,url):
        data = base_request.send_request("post",url, header= self.handle_info["Handler"]).json()
        logger.info(f'总充值:{data}')
        return data.get('data')



    '''
        根据表具编号获取表具ID
    '''
    def get_table_id(self,url,data):
        data = base_request.send_request("get",url, data=data,header= self.handle_info["Handler"]).json()
        logger.info(f'表具ID:{data}')
        return data.get('data')



    '''
        读数上报
    '''
    def get_report_data(self,url,data):
        data = base_request.send_request("post",url, data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'读数上报:{data}')
        return data


    '''
        历史记录
    '''
    def get_history_data(self,url,data):
        data = base_request.send_request("post",url, data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'历史记录:{data}')
        return data.get("data")


    '''
        抄表成功率
    '''
    def get_success_rate(self,url,data):
        data = base_request.send_request("post",url,data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'抄表成功率:{data}')
        return data

    '''
        用气量
    '''
    def get_gas_consumption(self,url,data):
        data = base_request.send_request("post",url,data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'用气量:{data}')
        return data


    '''
        用户信息
    '''
    def get_user_info(self,url):
        data = base_request.send_request("get",url,data=None, header= self.handle_info["Handler"]).json()
        logger.info(f'用户信息:{data}')
        return data

    '''
        计费信息8
        
    '''
    def get_config_info(self,url):
        data = base_request.send_request("get",url,data=None, header= self.handle_info["Handler"]).json()
        logger.info(f'计费信息:{data}')
        return data


    '''
        用户月用气量
    '''
    def get_user_customer_month(self,url,data):
        data = base_request.send_request("post",url,data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'用户月用气量:{data}')
        return data

    '''
        表具状态
    '''
    def get_table_state(self,url,data):
        data = base_request.send_request("post",url,data=json.dumps(data), header= self.handle_info["Handler"]).json()
        logger.info(f'表具状态:{data}')
        return data


request_data = RequestData()


