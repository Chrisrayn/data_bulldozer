# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    shopname = scrapy.Field()

    # month_sales = scrapy.Field()
    addr = scrapy.Field()
    # price = scrapy.Field()

