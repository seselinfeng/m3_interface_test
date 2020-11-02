#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import inspect
import hashlib

class GetCurrentItems(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        return __file__

    def get_current_class_name(self):
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        return sys._getframe().f_lineno


class GetRequestParas(object):
    """Request请求参数"""

    @staticmethod
    def para_filter(kwargs):
        sign_dict = {}
        for key, value in kwargs.items():
            if str(kwargs[key]) != '' and str(key) != 'sign' and str(key) != 'sign_type':
                sign_dict[key] = kwargs[key]
        print(sign_dict)
        return sorted(sign_dict.items(), key=lambda x: x[0])

    @staticmethod
    def create_link_string(sign_dict):
        pre_str = ''
        for key in sign_dict:
            pre_str = pre_str + str(key[0]) + '=' + str(key[1] + '&')
        else:
            pre_str = pre_str.rstrip('&')
        return pre_str

    @staticmethod
    def encryption(s):
        m = hashlib.md5()
        b = s.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5



if __name__ == '__main__':
    # pid: '1'
    #       requestTime: 1603974155208
    #       service: get_room_status_data
    #       sign: d7ab173dcff3c783170abdbd45641b01
    #       signType: MD5
    #       symbol: 4e349f7fb2ad48fbbb04245f916189af
    str_list = GetRequestParas.para_filter(service='get_room_status_data', signType='MD5',
                                           uticket='B12TGakun9m/ZPbyE1yL9FBfVeyWx01PP5IUCqvHG+c=',
                                           symbol='4e349f7fb2ad48fbbb04245f916189af', requestTime='1603974155208',
                                           pid='1')
    str = GetRequestParas.create_link_string(str_list)
    print(str)
    print(GetRequestParas.encryption(str))
