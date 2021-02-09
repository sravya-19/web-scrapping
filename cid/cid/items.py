# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CidItem(scrapy.Item):
	episode_number = scrapy.Field()
	episode_title = scrapy.Field()
	episode_date_channel = scrapy.Field()
	episode_desc = scrapy.Field()
