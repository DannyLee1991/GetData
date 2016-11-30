# coding=utf-8
import scrapy

from ..items import ESFItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class ESFDetailsSpider(scrapy.Spider):

    name = "esfdetails"
    allowed_domains = ["fang.com"]
    start_urls = [
        "http://esf.sh.fang.com/chushou/3_271653497.htm"
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    # id
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='title']/p[@class='gray9']/span[@class='mr10'][2]").extract()

    # publish time
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='title']/p[@class='gray9']").extract()

    # title
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='title']/h1").extract()

    # total_price
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='houseInfor clearfix']/div[@class='inforTxt']/dl/dt[@class='gray6 zongjia1']/span[@class='red20b']").extract()

    # house_type / house_build_area / house_use_area
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='houseInfor clearfix']/div[@class='inforTxt']/dl/dd[@class='gray6']").extract()

    #
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='houseInfor clearfix']/div[@class='inforTxt']/dl/dd[@class='gray6']").extract()
    # response.xpath("//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']/div[@class='houseInfor clearfix']/div[@class='inforTxt']/dl/dd")

    def parse(self, response):

        # path
        xpath = "//body/div[@class='wrap']/div[@class='main clearfix']/div[@class='mainBoxL']"
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
                print "户型==>"
                print i.strip()
            elif jzmj_str in str(i).encode("utf-8"):
                item['house_build_area'] = i.strip()
                print "建筑面积==>"
                print i.strip()
            elif symj_str in str(i).encode("utf-8"):
                item['house_use_area'] = i.strip()
                print "使用面积==>"
                print i.strip()
            elif nd_str in str(i).encode("utf-8"):
                item['house_age'] = i.strip()
                print "年代==>"
                print i.strip()
            elif cx_str in str(i).encode("utf-8"):
                item['orientation'] = i.strip()
                print "朝向==>"
                print i.strip()
            elif lc_str in str(i).encode("utf-8"):
                item['floor'] = i.strip()
                print "楼层==>"
                print i.strip()
            elif jg_str in str(i).encode("utf-8"):
                item['structure'] = i.strip()
                print "结构==>"
                print i.strip()
            elif zx_str in str(i).encode("utf-8"):
                item['decoration'] = i
                print "装修==>"
                print i
            elif zzlb_str in str(i).encode("utf-8"):
                item['residential_category'] = i.strip()
                print "住宅类别==>"
                print i.strip()
            elif jzlb_str in str(i).encode("utf-8"):
                item['building_class'] = i.strip()
                print "建筑类别==>"
                print i.strip()
            elif cqxz_str in str(i).encode("utf-8"):
                item['property_right'] = i.strip()
                print "产权性质==>"
                print i.strip()

        dt_infos = response.xpath(xpath + div_houseInfor_clearfix + div_inforTxt + dl + dt + "/a").extract()
        for i in dt_infos:
            if "查看此楼盘的更多二手房房源" in str(i).encode("utf-8"):
                item['property_name'] = i.strip()
                print "楼盘名称==>"
                print i.strip()
            elif "<span class=\"gray6 floatl\">学<span class=\"padl27\"></span>校：</span>" in str(i).encode("utf-8"):
                item['school'] = i.strip()
                print "学校==>"
                print i.strip()

        print "id ===> "
        print item['id']

        print "publish_time ===> "
        print item['publish_time']

        print "title ===> "
        print item['title']

        print "total_price ===> "
        print item['total_price']
