import json
import allure
import pytest

from testcase.test_base import TestBase
from utils.processingdata import get_data


@allure.feature("获取房态接口测试")
class TestGetRoomStatus(TestBase):
    @allure.title("测试接口是否正常")
    @pytest.mark.parametrize("test_room_status_data",
                             get_data("test_get_room_status_data", '../data/room_status_template.yaml'))
    def test_get_room_status_data(self, test_room_status_data, get_uticket):
        with allure.step("获取当前时间的时间戳"):
            test_room_status_data = self.get_time(test_room_status_data)
        with allure.step("将uticket sign 增加至请求参数中"):
            test_room_status_data = self.sign(get_uticket, test_room_status_data)
        with allure.step("发起https请求并获取返回数据"):
            r = self.room_status.get_room_status_data(test_room_status_data, get_uticket)
        r = json.loads(r.text)
        with allure.step("判断接口是否返回正确数据"):
            assert r['state'] == '200'
