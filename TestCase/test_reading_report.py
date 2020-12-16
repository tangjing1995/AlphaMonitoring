# -*- coding: UTF-8 -*-
import numpy as np
import pytest
from common.HandleTime import handle_time
from common.LoggerConfig import logger
from data.ConfigData import config_data
from data.RequestData import request_data

class TestReadingReport:

    @classmethod
    def setup_class(cls):
        logger.info("$读数上报检查$")

    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode", np.load('config/numpy/data.npy', allow_pickle=True))
    def test_reading_report(self,table_id,start_time,meter_reading,meterCode):
        logger.info("$读数上报--{}$".format(table_id))

        start_time,end_time= handle_time.update_data_time(start_time, 1)
        url,data = config_data.get_report_info(meterCode,start_time,end_time)
        results = request_data.get_report_data(url,data)
        if results["msg"] == "data节点数据为空":
            pytest.fail("表具:{},在{}:00:00 时间段左右没有上报数据".format(table_id,start_time))




