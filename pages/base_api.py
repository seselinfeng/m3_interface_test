import inspect
import json
from string import Template

import requests
import yaml


class BaseApi:
    def requests_http(self, req: json):
        """
        二次封装http请求
        :param req: 请求参数，包括且不限于 headers method data json
        :return: response
        """
        r = requests.request(**req)
        return r

    def template(self, test_data, data: dict):
        """
        模板替换变量
        :param test_data 测试数据
        :param data 需要参数化替代的数据
        :return 参数化后的数据
        """
        re = Template(test_data).safe_substitute(**data)
        return yaml.safe_load(re)

    def step(self, path: str = None):
        """
        封装操作步骤以及操作数据的数据驱动
        :param path:
        :return:
        """
        with open(path, encoding='utf-8') as f:
            # 获取调用函数名称
            name = inspect.stack()[1].function
            # 反射原理获取当前函数的yaml数据驱动
            steps = yaml.safe_load(f)[name][0]
            print("steps:{}".format(steps))
            # raw = json.dumps(steps)
            # print("raw:{}".format(raw))
            requests = steps.get("requests")
            # hooks = raw.get("hooks")
            return requests


if __name__ == '__main__':
    ba = BaseApi()
    ba.requests_http()
