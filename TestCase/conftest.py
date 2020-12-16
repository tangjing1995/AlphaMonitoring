#-*- coding: UTF-8 -*-
import pytest
from common.HandleIni import handle_ini
from common.LoggerConfig import logger

"""
    通过命令选择配置文件中 测试对象
"""

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config",
        help="this is config cmd")



@pytest.fixture(scope="session")
def config(request):
    return request.config.getoption("--config")



