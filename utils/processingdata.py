import yaml


def get_data(name, path):
    """
    获取对应方法的数据
    :param name: function name
    :param path: yaml path
    :return: data_list
    """
    return yaml.safe_load(open(path, encoding='utf-8')).get(name)


def add_uticket(data, uticket):
    """
    添加uticket
    :param data: 请求参数
    :param uticket: 用户uticket
    :return: 完整的请求参数
    """
    data['json']['uticket'] = uticket
    return data
