import time
import numpy as np
import pytest
from common.LoggerConfig import logger
from data.ConfigData import config_data
from data.RequestData import request_data
from data.Mock_Data import mock_data

class TestDosageCalculate:

    @classmethod
    def setup_class(cls):
        logger.info("$用量检查$")

    @pytest.mark.parametrize("table_id,start_time,meter_reading,meterCode", np.load('config/numpy/data.npy', allow_pickle=True))
    def test_reading_report(self,table_id,start_time,meter_reading,meterCode):
        logger.info("$用量检查--{}$".format(table_id))
        url,data = config_data.get_consump_tion_statistic(meterCode)

        results = request_data.get_gas_consumption(url,data)['data'][1]['value']
        print(request_data.get_gas_consumption(url,data)['data'])

        customerCode = request_data.get_user_info(config_data.get_user_info_ags(meterCode)).get('data')['customerCode']
        if not customerCode:
            pytest.skip("没有绑定用户跳过此表具")
        ct_url, ct_data = config_data.get_consumption_month(customerCode)

        ct_results = request_data.get_user_customer_month(ct_url,ct_data)['data'][-1]['consumptionGas']

        if results!= ct_results:
                pytest.fail("表具{}累计用气与报表累计用气不一致  \n\t用量统计:{}, 月累计用气:{}".format(table_id,results,ct_results))






