# encoding=utf8
__author__ = 'lijianan'

from http import send_get
import json
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
    # print(json_str)
    for i in json_str.split("&"):
        print("====")
        print(i)

get_fangjia("北京",year=10)
