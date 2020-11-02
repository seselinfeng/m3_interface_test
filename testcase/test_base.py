import time

from pages.login import Login
from pages.room_status import Room_Status
from utils.tools import GetRequestParas


class TestBase:
    def setup(self):
        self.login = Login()
        self.room_status = Room_Status()

    def sign(self, uticket, params):
        """
        增加签名
        :param uticket:
        :param params:
        :return:
        """
        # 增加uticket字段
        params['json']['uticket'] = uticket
        # 加签
        str_list = GetRequestParas.para_filter(params['json'])
        str = GetRequestParas.create_link_string(str_list)
        sign = GetRequestParas.encryption(str)
        # 增加签名字段
        params['json']['sign'] = sign
        return params

    def get_time(self, params):
        """
        获取当前时间的时间戳并追加到请求参数中
        :param params:
        :return:
        """
        params['json']['requestTime'] = str(round(time.time() * 1000))
        return params
