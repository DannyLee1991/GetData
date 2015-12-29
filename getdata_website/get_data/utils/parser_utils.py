__author__ = 'lijianan'
# coding:utf-8
import demjson

# return list: item is a map like :{'price': '7163', 'time': '1388505600000'}
def parse_json(json_str):
    s = str(json_str[1:-1]).replace('[','').replace(']','').split(',')
    list = []
    for i in range(len(s)):
        if i % 2 :
            list[i/2]["price"]=s[i]
        else:
            list.append({})
            list[i/2]["time"]=s[i]
    print(list)
    return list

def parse_city_data(data_file):
    f = open(data_file)
    s = f.read()
    json_obj = demjson.decode(s)
    print(json_obj[1]['province'])
    return json_obj