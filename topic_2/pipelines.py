# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import urllib.request

class Topic2Pipeline(object):
    def process_item(self, item, spider):
        """print ("        Item:          ",item)
#        for i in range(0, len(item['url'])):
        this_url = item['url']
#            print ("     this_url:       ",this_url)
        id = re.findall('http://724.169pp.net/169mm/(.*?).jpg', this_url)[0]
        id = id.replace('/', '_')
        File = '/home/miga/penglin_core/topic_2/img/' + id
        print('Downloading :' , File)
        urllib.request.urlretrieve(this_url, filename=File)
        print('Final Download :' , File)"""
        return item
