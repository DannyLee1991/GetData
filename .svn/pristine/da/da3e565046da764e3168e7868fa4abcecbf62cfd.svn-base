from django.db import models

# Create your models here.
# province city
# city time price_second_hand

class ProvCityManager(models.Manager):
    def get_citys_by_prov(self, prov):
        return self.filter(province=prov).values("city")

    def get_prov_by_city(self, city):
        return self.filter(city=city).values("province")

    def is_exist(self, prov, city):
        return len(self.filter(province=prov, city=city)) > 0

    def get_all_citys(self):
        city_list = []
        for item in self.distinct():
            city_list.append(item.city)
        return city_list

    def get_all_province(self):
        province_list = []
        for item in self.distinct():
            province_list.append(item.province)
        return set(province_list)

    def get_prov_city_dict_list(self):
        prov_city_dict_list = []
        for prov in self.get_all_province():
            city_list = self.get_citys_by_prov(prov)
            prov_city_dict_list.append({prov:city_list})
        return prov_city_dict_list

class OneHandHousingPriceManager(models.Manager):
    def save(self, city, time, price):
        if not self.is_exist(city, time, price):
            TimeHousingPriceOfOneHand(city=city, time=int(time), price=price).save()
            print("-------save--------city:" + str(city) + "---time:" + str(time) + "---price:" + str(price) + "---")

    def is_exist(self, city, time, price):
        return len(self.filter(city=city, time=time, price=price)) > 0

    def get_by_time(self, time):
        return self.filter(time = time).order_by("-price")

    def get_by_city(self, city):
        return self.filter(city = city).order_by("-time")

    def get_time_list(self):
        return self.values("time").distinct().order_by("-time").values("time")

    def get_city_info(self, city):
        return self.filter(city = city).order_by("-time")

class SecondHandHousingPriceManager(models.Manager):
    def save(self, city, time, price):
        if not self.is_exist(city, time, price):
            TimeHousingPriceOfSecondHand(city=city, time=int(time), price=price).save()
            print("-------save--------city:" + str(city) + "---time:" + str(time) + "---price:" + str(price) + "---")

    def is_exist(self, city, time, price):
        return len(self.filter(city=city, time=time, price=price)) > 0

    def get_by_time(self, time):
        return self.filter(time = time).order_by("-price")

    def get_by_city(self, city):
        return self.filter(city = city).order_by("-time")

    def get_time_list(self):
        return self.values("time").distinct().order_by("-time").values("time")

    def get_city_info(self, city):
        return self.filter(city = city).order_by("-time")

class ProvCity(models.Model):
    _id = models.IntegerField(primary_key=True, auto_created=True)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    objects = ProvCityManager()

    def __unicode__(self):
        return self.city


class TimeHousingPriceOfOneHand(models.Model):
    _id = models.IntegerField(primary_key=True, auto_created=True)
    city = models.CharField(max_length=20)
    time = models.CharField(max_length=15)
    price = models.IntegerField(default=0)

    objects = OneHandHousingPriceManager()

    class Meta:
        ordering = ['time']


class TimeHousingPriceOfSecondHand(models.Model):
    _id = models.IntegerField(primary_key=True, auto_created=True)
    city = models.CharField(max_length=20)
    time = models.CharField(max_length=15)
    price = models.IntegerField(default=0)

    objects = SecondHandHousingPriceManager()

    class Meta:
        ordering = ['time']
