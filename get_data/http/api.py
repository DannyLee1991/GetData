# encoding=utf8
__author__ = 'lijianan'

import sys, json.encoder
from json.encoder import JSONEncoder

from http import send_get,send_post
from ..utils.parser_utils import parse_json


reload(sys)
sys.setdefaultencoding('utf-8')

host = "http://fangjia.fang.com/"

path_get_fangjia = host + "pinggu/ajax/chartajax.aspx"

_default_encoder = JSONEncoder(
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    encoding='utf-8',
    default=None,
)

def get_fangjia(city,year=2,Class="defaultnew",dataType=3):
    params={"city":str(_default_encoder.encode(city)[1:-1]).replace("\\","%"),
            "year":year,
            "Class":Class,
            "dataType":dataType,}

    real_get_fangjia_path = path_get_fangjia + "?"

    for k in params:
        real_get_fangjia_path += str(k) + "=" + str(params[k]) + "&"

    real_get_fangjia_path = real_get_fangjia_path[:-1]

    json_str = send_post(real_get_fangjia_path,params_dict={})
    one_heand_info_list = second_heand_info_list = []

    print "---------------start---------------"
    print json_str
    print "---------------end---------------"

    for num, i in enumerate(json_str.split("&")):
        # print("====" + str(num))
        # print(i)
        if i:
            if num == 0:
                one_heand_info_list = parse_json(i)
            elif num == 1:
                second_heand_info_list = parse_json(i)
    return one_heand_info_list,second_heand_info_list

# get_fangjia("郑州",year=2)

# parse_city_data('../data/citys')