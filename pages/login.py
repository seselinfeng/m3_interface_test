# 在api package中是代表所有的接口信息的具体的实现，一个公共方法代表一个接口
from pages.base_api import BaseApi


class Login(BaseApi):

    def get_uticket(self, test_login_data):
        """获取stock存量"""
        # req = self.template(test_login_data, venv_data)
        r = self.requests_http(test_login_data)
        print(str(r.text))
        return r
