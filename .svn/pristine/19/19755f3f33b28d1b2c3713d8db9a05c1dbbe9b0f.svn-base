# coding:utf8
from django.shortcuts import render_to_response
from ..utils.parser_utils import parse_json, parse_city_data
from ..http.api import get_fangjia
from get_data.models import ProvCity, TimeHousingPriceOfOneHand, TimeHousingPriceOfSecondHand
import os, sys, json,time
import HTMLParser
from django.http import JsonResponse


def save_prov_citys_info():
    path = os.path.dirname(__file__) + os.sep + ".." + os.sep + "data" + os.sep + "citys"
    prov_citys_list = parse_city_data(path)
    for prov_citys in prov_citys_list:
        prov = prov_citys["province"]
        for city in prov_citys["city_list"]:
            # city = unicode(city)
            if not ProvCity.objects.is_exist(prov=prov, city=city):
                ProvCity(province=prov, city=city).save()


def crawls_and_save_info():
    city_list = ProvCity.objects.get_all_citys()
    for city in city_list:
        one_hand_housing_price, second_hand_housing_price = get_fangjia(city, 10)
        for item in one_hand_housing_price:
            try:
                price = item["price"]
                time = item["time"]
                TimeHousingPriceOfOneHand.objects.save(city, time, price)
            except KeyError:
                print("key error")

        for item in second_hand_housing_price:
            try:
                price = item["price"]
                time = item["time"]
                TimeHousingPriceOfSecondHand.objects.save(city, time, price)
            except KeyError:
                print("key error")


def index(request):
    province_city_dict_list = ProvCity.objects.get_prov_city_dict_list()
    city_infos_of_one_hand = []
    city_infos_of_second_hand = []
    city = ""

    if 'city' in request.GET:
        city = request.GET['city']
        for num, data in enumerate(TimeHousingPriceOfOneHand.objects.get_city_info(city).values("time", "price")[::-1]):
            t = long(data["time"][0:-3])
            x = time.localtime(t)
            time_str = time.strftime('%Y-%m-%d',x)
            data_time = ''.join(map(lambda x: "%c" % ord(x), time_str))
            data_time = HTMLParser.HTMLParser().unescape(data_time)

            price = data["price"]
            city_infos_of_one_hand.append({"time":data_time,"price":price})
            # print("(" + str(num) + ")" + " -- " + str(data["price"]) + "--" + str(long(data["time"])) + "----" )
        city_infos_of_one_hand = HTMLParser.HTMLParser().unescape(city_infos_of_one_hand)

        for num, data in enumerate(TimeHousingPriceOfSecondHand.objects.get_city_info(city).values("time", "price")[::-1]):
            t = long(data["time"][0:-3])
            x = time.localtime(t)
            time_str = time.strftime('%Y-%m-%d',x)
            data_time = ''.join(map(lambda x: "%c" % ord(x), time_str))
            data_time = HTMLParser.HTMLParser().unescape(data_time)

            price = data["price"]
            city_infos_of_second_hand.append({"time":data_time,"price":price})
        city_infos_of_second_hand = HTMLParser.HTMLParser().unescape(city_infos_of_second_hand)



    # save_prov_citys_info()
    # crawls_and_save_info()

    # 获取1446307200000时间的所有城市的一手房房价信息
    # data_set = TimeHousingPriceOfOneHand.objects.get_by_time("1446307200000").values("city","time","price")
    # print(data_set)
    # for num, data in enumerate(data_set):
    # print( "("+str(num)+")" + data["city"] + " -- " + str(data["price"]) +"------" )

    # 获取所有时间值
    # time_list = TimeHousingPriceOfOneHand.objects.get_time_list()
    # for t in time_list:
    # print(t)

    # city_list = ProvCity.objects.get_all_citys()
    # for num_city, city in enumerate(city_list):
    #     print("("+ str(num_city) +")" + city + "------")
    #     city_infos = TimeHousingPriceOfOneHand.objects.get_city_info(city).values("city","time","price")
    #     for num, data in enumerate(city_infos):
    #         print("("+str(num)+")" + data["city"] + " -- " + str(data["price"]) +"--" + str(data["time"]) + "----" )



    return render_to_response('index.html',
                              {"province_city_dict_list": province_city_dict_list,
                               "city_infos_of_one_hand": city_infos_of_one_hand,
                               "city_infos_of_second_hand": city_infos_of_second_hand,
                               "city":city,
                              })
