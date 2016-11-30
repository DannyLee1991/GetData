# coding=utf-8
from django.test import TestCase

# Create your tests here.
import json, time
import urllib, httplib, urlparse


def send_http(url, params_dict={}, headers={}, method='GET'):
    host = urlparse.urlparse(url).hostname
    conn = httplib.HTTPConnection(host)
    if params_dict:
        url += "?" + urllib.urlencode(params_dict)
    conn.request(method=method, url=url, body=urllib.urlencode(params_dict), headers=headers)
    response = conn.getresponse()
    res = response.read()
    return res


def send_post(url, params_dict={}, headers={}):
    return send_http(url, params_dict, headers, method='POST')

#
# l = [{"a",1,},{"ba",2,},]
#
# print json.dumps(l)

#
# data1 = [{'city': u'\u8d35\u9633'}, {'city': u'\u9075\u4e49'}, {'city': u'\u9ed4\u4e1c\u5357'}, {'city': u'\u5b89\u987a'}, {'city': u'\u9ed4\u5357'}, {'city': u'\u6bd5\u8282'}, {'city': u'\u94dc\u4ec1'}, {'city': u'\u516d\u76d8\u6c34'}, {'city': u'\u9ed4\u897f\u5357'}, {'city': u'\u51ef\u91cc'}, {'city': u'\u5f00\u9633'}, {'city': u'\u4fee\u6587'}, {'city': u'\u6e05\u9547'}]
#
# encode_json = json.dumps(data1)
# print type(encode_json), encode_json
#
# data = long("1448899200000"[0:-3])
# x = time.localtime(data)
# print time.strftime('%Y-%m-%d %H:%M:%S',x)

url = "http://fangjia.fang.com/pinggu/ajax/chartajax.aspx?dataType=3&city=%u4E0A%u6D77&Class=defaultnew&year=1"

# 定义一个要提交的数据数组(字典)
params = {}

result = send_post(url=url,params_dict=params)
print result
