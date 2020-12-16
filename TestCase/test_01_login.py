# -*- coding: UTF-8 -*-
import pytest
import numpy as np
from common.LoggerConfig import logger
from data.RequestData import request_data
from data.ConfigData import config_data


class Testlogin:

    @classmethod
    def setup_class(cls):
        logger.info("$登录模块$")
        cls.info_items = []
        cls.data = []



    def test_login(self,config):
        logger.info("$登录$")
        url,data = config_data.get_user_info(config)
        request_data.login(url,data)



    @pytest.mark.parametrize("table_id,start_time,meter_reading",config_data.get_table_all_data())
    def test_meter_code(self,table_id,start_time,meter_reading):
        logger.info("$ID获取--{}$".format(table_id))
        self.info_items = []
        url, data = config_data.get_table_info(table_id)
        results = request_data.get_table_id(url, data)
        self.info_items.append(table_id)
        self.info_items.append(start_time)
        self.info_items.append(meter_reading)
        self.info_items.append(results["meterId"])
        self.data.append(self.info_items)




    def teardown_class(self):
        data  = np.array(self.data)
        np.save('config/numpy/data.npy', data)
