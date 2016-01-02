from django.test import TestCase

# Create your tests here.
import json,time
#
# l = [{"a",1,},{"ba",2,},]
#
# print json.dumps(l)
data1 = [{'city': u'\u8d35\u9633'}, {'city': u'\u9075\u4e49'}, {'city': u'\u9ed4\u4e1c\u5357'}, {'city': u'\u5b89\u987a'}, {'city': u'\u9ed4\u5357'}, {'city': u'\u6bd5\u8282'}, {'city': u'\u94dc\u4ec1'}, {'city': u'\u516d\u76d8\u6c34'}, {'city': u'\u9ed4\u897f\u5357'}, {'city': u'\u51ef\u91cc'}, {'city': u'\u5f00\u9633'}, {'city': u'\u4fee\u6587'}, {'city': u'\u6e05\u9547'}]

encode_json = json.dumps(data1)
print type(encode_json), encode_json

data = long("1448899200000"[0:-3])
x = time.localtime(data)
print time.strftime('%Y-%m-%d %H:%M:%S',x)