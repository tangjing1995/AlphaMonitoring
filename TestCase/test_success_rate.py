# -*- coding: UTF-8 -*-
import time
import numpy as np
import pytest
from common.LoggerConfig import logger
from data.ConfigData import config_data
from data.RequestData import request_data
from data.Mock_Data import mock_data
class TestSuccessRate:

    @classmethod
    def setup_class(cls):
        logger.info("$上报成功率模块$")
        cls.no_time_report ={}

    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode",np.load('config/numpy/data.npy', allow_pickle=True))
    def test_history_data(self,table_id,start_time,meter_reading,meterCode):
        logger.info("$历史记录--{}$".format(table_id))

        report_time_list =[]
        no_report_item=[]
        url,data = config_data.get_history_data_info(meterCode)
        results = request_data.get_history_data(url,data)

        for i in results:
            timeArray = time.localtime(int(i["readingTime"]*0.001))
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            report_time_list.append(otherStyleTime)

        start_time = start_time.split(":")[0]
        for item in mock_data.mock_history_time(int(start_time)):
            if item not in report_time_list:
                no_report_item.append(item)
        self.no_time_report[table_id] = no_report_item
        if len(self.no_time_report[table_id])>0:
            pytest.fail(f"表具{table_id}:历史记录整点未抄表时间点:\n{self.no_time_report[table_id]}")




    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode",np.load('config/numpy/data.npy', allow_pickle=True))
    def test_success_rate(self,table_id,start_time,meter_reading,meterCode):

        logger.info("$上报成功率--{}$".format(table_id))
        url,data = config_data.get_success_rate_info(meterCode)
        results = request_data.get_success_rate(url,data)
        if results["msg"] == "data节点数据为空":
            pytest.fail("表具{}:在{} 时间段内没有上报数据".format(table_id,start_time))
        success_rate = (24 - len(self.no_time_report[table_id]))/ 24
        assert success_rate == results["data"][0]["value"] ,table_id



