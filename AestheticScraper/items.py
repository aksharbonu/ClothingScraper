# -*- coding: utf-8 -*-

import scrapy

class ClothingItem(scrapy.Item):
    image = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
