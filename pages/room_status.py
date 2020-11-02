from pages.base_api import BaseApi
from utils.processingdata import add_uticket


class Room_Status(BaseApi):
    def get_room_status_data(self, test_room_status_data, uticket):
        """获取房态"""
        test_stock_data = add_uticket(test_room_status_data, uticket)
        r = self.requests_http(test_stock_data)
        return r
