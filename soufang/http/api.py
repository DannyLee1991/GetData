# encoding=utf8
__author__ = 'lijianan'

from http import send_get
from soufang.utils.parser_utils import parse_json,parse_city_data
import sys

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
    for num, i in enumerate(json_str.split("&")):
        print("====" + str(num))
        print(i)
        if num <= 1 and i:
            parse_json(i)

# get_fangjia("文山",year=2)
parse_city_data('../data/citys')