__author__ = 'lijianan'

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
        # time = i[0]
        # price = i[1]
        # print(time)
        # print(price)