from django.shortcuts import render_to_response
from ..utils.parser_utils import parse_json, parse_city_data
from ..http.api import get_fangjia
from get_data.models import ProvCity,TimeHousingPriceOfOneHand,TimeHousingPriceOfSecondHand
import os,sys


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
    # save_prov_citys_info()
    # ProvCityManager.
    crawls_and_save_info()

    return render_to_response('index.html')
