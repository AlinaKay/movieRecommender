# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title=scrapy.Field()
    # link=scrapy.Field()
    # desc=scrapy.Field()
	title=scrapy.Field()
	title_href=scrapy.Field()
	year_type=scrapy.Field()
	user_rating=scrapy.Field()
	rating_rating=scrapy.Field()
	outline=scrapy.Field()
	credit_dir=scrapy.Field()
	credit_with=scrapy.Field()
	genre=scrapy.Field()
	mins=scrapy.Field()