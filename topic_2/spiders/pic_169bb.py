# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from topic_2.items import Topic2Item
import re

class Pic169bbSpider(scrapy.Spider):
    name = 'pic_169bb'
    allowed_domains = ['169bb.com','169tp.com','724.169pp.net']
    start_urls = ['http://www.169tp.com/']
    

    def parse(self, response):
        urldata = response.xpath("//div[@class='w1000']/a/@href").extract()
        xiyangurldata = urldata[5]
        yield Request(url=xiyangurldata, callback=self.next1)

    def next1(self, response):
        page_url_list = response.xpath('//div[@class="page"]/ul/li/a/@href').extract()
        for i in range(len(page_url_list)):
            page_url_list[i] = response.url + page_url_list[i]
        page_url_list.append(response.url)
        for url in page_url_list:
           yield Request(url=url, callback=self.next2)

    def next2(self,response):
        meinv_url_list = response.xpath('//ul[@class="product01"]/li/a/@href').extract()
        for url in meinv_url_list:
            yield Request(url=url,callback=self.next3)

    def next3(self,response):
        last_page_url = response.xpath('//ul[@class="pagelist"]/li/a/@href').extract()[-2]
        pat = re.compile(r'http://www.169(.*).com/guoneimeinv/(.*/.*)/(.*)\.html')
        m = pat.match(response.url)
        last_page_url = 'http://www.169'+ m.group(1)+'.com/guoneimeinv/'+m.group(2)+'/'+ last_page_url
#        print ("last_page_url",last_page_url)
        yield Request(url=last_page_url,callback=self.next4)
    
    def next4(self, response):
        last_img_url = response.xpath('//div[@class="big_img"]/p/img/@src').extract()[-1]
        pat = re.compile(r'http://724.169pp.net/169mm/(.*/.*)/(.*)\.jpg')
        m = pat.match(last_img_url)
        num = int(m.group(2))
        img_url_list = []
        for i in range(1,num+1):
            img_url_list.append('http://724.169pp.net/169mm/'+ m.group(1) + '/'+str(i)+'.jpg')
        item = Topic2Item()
        item['image_urls'] = img_url_list
        yield item
        

    def GetImg(self,response):
        item = Topic2Item()
#        item['url'] = response.url
#        print ('最终URL：',item['url'])
        yield item