# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Topic2Item(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()