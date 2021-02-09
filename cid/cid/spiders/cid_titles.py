import scrapy
from ..items import CidItem
# import pdb


class CidTitlesSpider(scrapy.Spider):
	name = 'cid_titles'
	# allowed_domains = ['https://www.thetvdb.com/series/c-i-d/allseasons/official']
	start_urls = ['https://www.thetvdb.com/series/c-i-d/allseasons/official/']

	custom_settings = {'FEED_URI': "cid_titles_%(time)s.csv", 'FEED_FORMAT': 'csv'}

	def parse(self, response):

		episodes = response.css("li.list-group-item")

		episode_obj = CidItem()

		for episode in episodes:

			episode_number = episode.css('span.text-muted').css('.episode-label::text').extract()

			if len(episode_number) == 0:
				episode_obj['episode_number'] = ''
			else:
				episode_obj['episode_number'] = episode_number[0]

			episode_title = episode.css('a::text').extract()
			episode_title = [title.strip() for title in episode_title if title.strip() != '' and title.strip() != 'Unknown']

			if len(episode_title) == 0:
				episode_obj['episode_title'] = ''
			else:
				episode_obj['episode_title'] = episode_title[0]

			episode_date_channel = episode.css('ul.list-inline').css('li::text').extract()

			if len(episode_date_channel) == 0:
				episode_obj['episode_date_channel'] = ''
			else:
				episode_obj['episode_date_channel'] = '; '.join(episode_date_channel)

			episode_desc = episode.css('div.list-group-item-text').css('div.row').css('div.col-xs-9').css('p::text').extract()

			if len(episode_desc) == 0:
				episode_obj['episode_desc'] = ''
			else:
				episode_obj['episode_desc'] = episode_desc[0]

			yield episode_obj
