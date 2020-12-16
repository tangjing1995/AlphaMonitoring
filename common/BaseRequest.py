# -*- coding: UTF-8 -*-
import requests

class BaseRequest(object):

    def __init__(self):
        self.session = requests.session()
        self.session.DEFAULT_RETRIES = 5
        self.session.keep_alive = False


    def send_get(self,url,data,cookie,header):
        res = self.session.get(url=url, params=data,cookies=cookie, headers=header,verify=False)
        return res

    def send_post(self, url, data, cookie,get_cookie, header):
        res = self.session.post(url=url, data=data,cookies=cookie, headers=header,verify=False)
        if get_cookie != None:
            cookie_value = requests.utils.dict_from_cookiejar(self.session.cookies)
            return cookie_value
        return res

    def send_request(self,method, url, data=None,cookie=None, header=None):
        requests.packages.urllib3.disable_warnings()
        if method=="get":
            return self.send_get(url,data,cookie,header)
        else:
            return self.send_post(url, data,cookie, header)

base_request = BaseRequest()