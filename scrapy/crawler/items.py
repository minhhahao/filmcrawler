# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class CrawlerItem(Item):
    product_name = Field()
    product_url = Field()
    description_urls = Field()
    description = Field()
    title = Field()
    post_date = Field()
    image_urls = Field()
    categories = Field()
    tags = Field()
