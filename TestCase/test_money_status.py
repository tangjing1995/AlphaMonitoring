# -*- coding: UTF-8 -*-
import numpy as np
import pytest
from common.LoggerConfig import logger
from data.ConfigData import config_data
from data.RequestData import request_data

class TestMoneyStatus:


    @classmethod
    def setup_class(cls):
        logger.info("$金额校验$")

    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode", np.load('config/numpy/data.npy', allow_pickle=True))
    def test_money_status(self, table_id, start_time, meter_reading, meterCode):
        logger.info("$金额校验--{}$".format(table_id))
        table_info = request_data.get_user_info(config_data.get_user_info_ags(meterCode)).get('data')
        if not table_info['customerCode']:
            pytest.skip("没有绑定用户跳过此表具")

        config_info = request_data.get_config_info(config_data.get_config_info_data(meterCode)).get('data')
        if config_info['billingMode']=='1':
            if table_info['balance']<10:
                pytest.fail("表具:{} 目前余额:{}".format(table_id,table_info['balance']))
