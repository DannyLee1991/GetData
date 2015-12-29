# encoding=utf8
__author__ = 'lijianan'

import sys

from http import send_get
from ..utils.parser_utils import parse_json


reload(sys)
sys.setdefaultencoding('utf-8')

host = "http://fangjia.fang.com/"

path_get_fangjia = host + "pinggu/ajax/chartajax.aspx"


def get_fangjia(city,year=2,Class="defaultnew",dataType=3):
    params={"city":city.encode("gbk"),
            "year":year,
            "Class":Class,
            "dataType":dataType,}

    json_str = send_get(path_get_fangjia,params_dict=params)
    one_heand_info_list = second_heand_info_list = []
    for num, i in enumerate(json_str.split("&")):
        print("====" + str(num))
        print(i)
        if i:
            if num == 0:
                one_heand_info_list = parse_json(i)
            elif num == 1:
                second_heand_info_list = parse_json(i)
    return one_heand_info_list,second_heand_info_list

# get_fangjia("郑州",year=2)

# parse_city_data('../data/citys')