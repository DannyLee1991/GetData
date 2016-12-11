# coding=utf-8
import random

import scrapy

from ..items import ESFItem
from ..utils.Log import log_i

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ESFListSpider(scrapy.Spider):
    name = "esflist"

    # allowed_domains = ["fang.com"]

    base_url = "http://esf.sh.fang.com/map/?mapmode=y&orderby=30&ecshop=ecshophouse&PageNo=$&a=ajaxSearch&city=sh&searchtype=loupan"
    start_urls = []
    for i in range(2, 100):
        start_urls.append(str(base_url).replace("$", str(i)))

    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        infos = response.xpath("//a/@href").extract()

        index = 0
        size = len(infos)

        for i in infos:
            i_str = str(i).encode("utf-8")
            if "esf" in i_str:
                url = i_str.replace('\\', '').strip()
                index += 1
                log_i("==url:" + url + " ====================progress: " + str(index) + "/" + str(size) + "=======")

                yield scrapy.Request(url=url.replace("\"", ""), callback=self.parse_details)

    def parse_details(self, response):
        log_i("+++++++++++++被执行了+++++++++++++++++++")


        # path
        xpath = "//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']"
        xpath_bread = "//body/div[@class='wrap']/div[@class='bread']/p[@class='floatl']"
        div_title = "/div[@class='title']"
        p_gray9 = "/p[@class='gray9']"
        h1 = "/h1"
        span_mr10 = "/span[@class='mr10']"
        div_houseInfor_clearfix = "/div[@class='houseInfor clearfix']"
        div_inforTxt = "/div[@class='inforTxt']"
        dl = "/dl"
        dt_gray6_zongjia1 = "/dt[@class='gray6 zongjia1']"
        span_red20b = "/span[@class='red20b']"
        dd_gray6 = "/dd[@class='gray6']"
        dd = "/dd"
        dt = "/dt"

        item = ESFItem()
        item['url'] = response.url

        bread_list = response.xpath("//body/div[@class='wrap']/div[@class='bread']/p[@class='floatl']/a").extract()
        for index,bread in enumerate(bread_list[1:]):
            if index == 0:
                item["bread_city"] = bread
            elif index == 1:
                item["bread_area"] = bread
            elif index == 2:
                item["bread_positon"] = bread

        item['id'] = response.xpath(xpath +
                                    div_title +
                                    p_gray9 +
                                    span_mr10).extract_first().strip()

        item['publish_time'] = response.xpath(xpath +
                                              div_title +
                                              p_gray9).extract_first().strip()

        item['title'] = response.xpath(xpath +
                                       div_title +
                                       h1).extract_first().strip()

        item['total_price'] = response.xpath(xpath +
                                             div_houseInfor_clearfix +
                                             div_inforTxt +
                                             dl +
                                             dt_gray6_zongjia1 +
                                             span_red20b).extract_first().strip()

        dd_infos = response.xpath(xpath + div_houseInfor_clearfix + div_inforTxt + dl + dd).extract()
        huxing_str = "<span class=\"gray6\">户<span class=\"padl27\"></span>型："
        jzmj_str = "<dd class=\"gray6\">建筑面积：<span class=\"black \">"
        symj_str = "<dd class=\"gray6\">使用面积：<span class=\"black \">"
        nd_str = "<span class=\"gray6\">年<span class=\"padl27\"></span>代：</span>"
        cx_str = "<span class=\"gray6\">朝<span class=\"padl27\"></span>向：</span>"
        lc_str = "<span class=\"gray6\">楼<span class=\"padl27\"></span>层：</span>"
        jg_str = "<span class=\"gray6 \">结<span class=\"padl27\"></span>构：</span>"
        zx_str = "<span class=\"gray6\">装<span class=\"padl27\"></span>修：</span>"
        zzlb_str = "<span class=\"gray6\">住宅类别：</span>"
        jzlb_str = "<span class=\"gray6\">建筑类别：</span>"
        cqxz_str = "<span class=\"gray6 \">产权性质：</span>"

        for i in dd_infos:
            if huxing_str in str(i).encode("utf-8"):
                item['house_type'] = i.strip()
                log_i("户型==>")
                log_i(i.strip())
            elif jzmj_str in str(i).encode("utf-8"):
                item['house_build_area'] = i.strip()
                log_i("建筑面积==>")
                log_i(i.strip())
            elif symj_str in str(i).encode("utf-8"):
                item['house_use_area'] = i.strip()
                log_i("使用面积==>")
                log_i(i.strip())
            elif nd_str in str(i).encode("utf-8"):
                item['house_age'] = i.strip()
                log_i("年代==>")
                log_i(i.strip())
            elif cx_str in str(i).encode("utf-8"):
                item['orientation'] = i.strip()
                log_i("朝向==>")
                log_i(i.strip())
            elif lc_str in str(i).encode("utf-8"):
                item['floor'] = i.strip()
                log_i("楼层==>")
                log_i(i.strip())
            elif jg_str in str(i).encode("utf-8"):
                item['structure'] = i.strip()
                log_i("结构==>")
                log_i(i.strip())
            elif zx_str in str(i).encode("utf-8"):
                item['decoration'] = i
                log_i("装修==>")
                log_i(i.strip())
            elif zzlb_str in str(i).encode("utf-8"):
                item['residential_category'] = i.strip()
                log_i("住宅类别==>")
                log_i(i.strip())
            elif jzlb_str in str(i).encode("utf-8"):
                item['building_class'] = i.strip()
                log_i("建筑类别==>")
                log_i(i.strip())
            elif cqxz_str in str(i).encode("utf-8"):
                item['property_right'] = i.strip()
                log_i("产权性质==>")
                log_i(i.strip())

        dt_infos = response.xpath(xpath + div_houseInfor_clearfix + div_inforTxt + dl + dt + "/a").extract()
        for i in dt_infos:
            if "查看此楼盘的更多二手房房源" in str(i).encode("utf-8"):
                item['property_name'] = i.strip()
                log_i("楼盘名称==>")
                log_i(i.strip())
            elif "<span class=\"gray6 floatl\">学<span class=\"padl27\"></span>校：</span>" in str(i).encode("utf-8"):
                item['school'] = i.strip()
                log_i("学校==>")
                log_i(i.strip())

        log_i("id ===> ")
        log_i(item['id'])

        log_i("publish_time ===> ")
        log_i(item['publish_time'])

        log_i("title ===> ")
        log_i(item['title'])

        log_i("total_price ===> ")
        log_i(item['total_price'])
        yield item
