# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ESFItem(scrapy.Item):
    # url
    url = scrapy.Field()
    # 房源编号
    id = scrapy.Field()
    # 发布时间
    publish_time = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 房型
    house_type = scrapy.Field()
    # 建筑面积
    house_build_area = scrapy.Field()
    # 使用面积
    house_use_area = scrapy.Field()
    # 年代
    house_age = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 结构
    structure = scrapy.Field()
    # 装修
    decoration = scrapy.Field()
    # 住宅类别
    residential_category = scrapy.Field()
    # 建筑类别
    building_class = scrapy.Field()
    # 产权性质
    property_right = scrapy.Field()
    # 楼盘名称
    property_name = scrapy.Field()
    # 学校
    school = scrapy.Field()
    # 配套设施
    supporting_facilities = scrapy.Field()

    # 城市 - 面包屑导航
    bread_city = scrapy.Field()
    # 区域 - 面包屑导航
    bread_area = scrapy.Field()
    # 位置 - 面包屑导航
    bread_positon = scrapy.Field()

    pass
