#coding: UTF-8
import pytest
import os,time
from common.SmtpReport import SmtpReport

workpath=os.path.abspath(os.path.join(os.path.dirname(__file__))) #py工程路径
now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
report_html=workpath+"\\Report\\report"+now+".html"

## 选择邮件接收人
send_to = ["tangjin@fiorentini.com.cn"]
sr = SmtpReport(send_to)
# 邮件主题
subject = "Phase2.0自动化Smoke测试报告"

if __name__ == '__main__':

    pytest.main([ "-s",'TestCase\\test_01_login.py',  "--config", "alpha-config", "--pytest_report", report_html, #"-m","addmeter",deletemeter
        "--pytest_title", "自动化测试报告",
        "--pytest_desc", "----智燃云SmartHippo--- ",
        "--pytest_fw", "1.0",
        "--pytest_web","1.0",
        "--pytest_LDN","1.0"])

    # sr.email_image_send(report_html, subject)





