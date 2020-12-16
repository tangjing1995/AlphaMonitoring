# -*- coding: UTF-8 -*-
import numpy as np
import pytest
from common.LoggerConfig import logger
from data.ConfigData import config_data
from data.RequestData import request_data

class TestvalveStatus:


    @classmethod
    def setup_class(cls):
        logger.info("$表具状态校验$")

    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode",np.load('config/numpy/data.npy', allow_pickle=True))
    def test_valve_status(self, table_id,start_time,meter_reading,meterCode):
        logger.info("$阀门状态验证--{}$".format(table_id))
        table_info = request_data.get_user_info(config_data.get_user_info_ags(meterCode)).get('data')

        if  table_info["valveStatus"] == '1':
            pytest.fail("表具{}:阀门关闭".format(table_id))


    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode",np.load('config/numpy/data.npy', allow_pickle=True))
    def test_electricity_status(self, table_id,start_time,meter_reading,meterCode):
        logger.info("$电量状态验证--{}$".format(table_id))
        table_info = request_data.get_user_info(config_data.get_user_info_ags(meterCode)).get('data')
        if  float(table_info["electricQuantity"]) < 5:
            pytest.fail("表具{}:电量接近耗尽,当前电量 {}%".format(table_id,table_info["electricQuantity"]))


    # @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode",np.load('config/numpy/data.npy', allow_pickle=True))
    # def test_table_status(self, table_id,start_time,meter_reading,meterCode):
    #     logger.info("$表具状态--{}$".format(table_id))
    #     url, data = config_data.get_table_state_data(table_id)
    #     result = request_data.get_table_state(url,data)
    #     if result['msg']=="查询成功":
    #         table_info = result.get("data")[0]
    #         if table_info["abnormalStatusText"] != None and table_info["abnormalStatusText"] !="欠费":
    #             pytest.fail("表具{}:状态异常，当前状态：{}".format(table_id,table_info["abnormalStatusText"]))
    #     else:
    #         pytest.skip("请求异常,请重试")

