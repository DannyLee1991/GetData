from get_data.models import ProvCity, TimeHousingPriceOfOneHand, TimeHousingPriceOfSecondHand

__author__ = 'lijianan'
from ..http.api import get_fangjia
from django.shortcuts import render_to_response

def spider(request):
    if 'crawls' in request.GET:
        if request.GET["crawls"] == "city_info":
            print "ooooo"
            crawls_and_save_info()
    return render_to_response("spider.html")

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