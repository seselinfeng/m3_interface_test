import pytest

from pages.base_api import BaseApi

ba = BaseApi()


@pytest.fixture(scope='session')
def manager_login(request):
    """
    :return:
    """
    response = ba.requests_http(request.param)
    return response.text


@pytest.fixture(scope='session')
def get_uticket():
    return "B12TGakun9m/ZPbyE1yL9GVt4mYA4zapWSNLfVQrOPo="
