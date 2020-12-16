# -*- coding: UTF-8 -*-
import datetime
import os
import json
from common.HandleExec import HandleExec
from common.HandleIni import handle_ini
from common.HandleTime import handle_time
from common.LoggerConfig import logger
from local_info import *


class ConfigData:

    def __init__(self):
        self.local_face_cfg = HandleExec(file_path=LOCAl_FACE_PATH)
        self.table_cfg = HandleExec(file_path=TABLE_CONFIG_PATH)



    #用户登录 数据
    def get_user_info(self,config):
        os.environ["host"] = handle_ini.get_content(config, "host")
        os.environ["companyAccount"] = handle_ini.get_content(config, "companyAccount")
        os.environ["account"] = handle_ini.get_content(config, "account")
        os.environ["password"] = handle_ini.get_content(config, "password")
        logger.info("当前测试配置:\n域名:{}\n燃气公司:{}\n账号:{}\n密码:{}"
                            .format(os.getenv("host"), os.getenv("companyAccount"), os.getenv("account"),
                                    os.getenv("password")))
        url = self.local_face_cfg.get_data(1)[0]
        user_data = json.loads(self.local_face_cfg.get_data(1)[1])

        user_data["companyAccount"] = os.getenv("companyAccount")
        user_data["account"] = os.getenv("account")
        user_data["password"] = os.getenv("password")
        return os.getenv("host")+url,user_data



    #获取表具ID 数据
    def get_table_info(self,table):
        url,data = self.get_local_data(5)
        table_data = json.loads(data)
        table_data["meterCode"] = table
        return os.getenv("host")+url,table_data


    #获取读数上报 数据
    def get_report_info(self,meter_code,start_time,end_time):
        url,data = self.get_local_data(6)
        report_data = json.loads(data)
        report_data["meterId"] = meter_code
        report_data["startTime"] = handle_time.update_specified_time(hour=start_time, minute="00", second="00")
        report_data["endTime"] =handle_time.update_specified_time(hour=end_time,minute="00",second="00")
        return os.getenv("host")+url,report_data;


    #获取抄表成功率 数据
    def get_success_rate_info(self,meter_code):
        url,data = self.get_local_data(9)
        report_data = json.loads(data)
        report_data["meterId"] = meter_code
        report_data["endTime"] =handle_time.update_specified_time(day=-1,hour="23",minute="59",second="59")
        report_data["startTime"] = handle_time.update_specified_time(day=-1,hour="00",minute="00",second="00")
        return os.getenv("host")+url,report_data


    #获取历史 数据
    def get_history_data_info(self,meter_code):
        url,data = self.get_local_data(7)
        report_data = json.loads(data)
        report_data["meterId"] = meter_code
        report_data["endTime"] =handle_time.update_specified_time(hour="01",minute="00",second="00")
        report_data["startTime"] = handle_time.update_specified_time(day=-1,hour="00",minute="00",second="00")
        return os.getenv("host")+url,report_data


    #获取用气量
    def get_consump_tion_statistic(self,meter_code):
        url,data = self.get_local_data(10)
        report_data = json.loads(data)
        report_data["meterId"] = meter_code
        report_data["startTime"] =handle_time.update_specified_time(day=-2,hour="00",minute="00",second="00")
        report_data["endTime"] =handle_time.update_specified_time(hour="00",minute="00",second="00")
        return os.getenv("host")+url,report_data


    #获取表具信息
    def get_user_info_ags(self,meter_code):
        url = self.get_local_data(11)
        return os.getenv("host")+url[0]+meter_code


    #获取用气量
    def get_consumption_month(self,customerCode):
        url,data = self.get_local_data(12)
        now = datetime.datetime.now()
        month = now.month
        if month<10:
            month='0'+str(now.month)
        report_data = json.loads(data)
        report_data["customerCode"] = customerCode
        report_data["month"] =str(now.year)+'-'+str(month)
        return os.getenv("host")+url,report_data


    #获取计费信息数据
    def get_config_info_data(self,meter_code):
        url = self.get_local_data(13)
        return os.getenv("host")+url[0]+meter_code

        # 获取用气量

    def get_table_state_data(self, meterCode):
        url, data = self.get_local_data(14)
        report_data = json.loads(data)
        report_data["meterCode"] = meterCode
        return os.getenv("host") + url, report_data

    def get_local_data(self,index):
        return self.local_face_cfg.get_data(index)


    def get_table_all_data(self):
        return self.table_cfg.get_vertical_all_value()




config_data = ConfigData()
