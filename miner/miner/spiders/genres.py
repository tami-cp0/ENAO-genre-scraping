import scrapy

class GenresSpider(scrapy.Spider):
    name = "genres"
    allowed_domains = ["everynoise.com"]
    start_urls = ['https://www.everynoise.com/everynoise1d.html']
    custom_settings = { 'ROBOTSTXT_OBEY': False }

    def parse(self, response):
        for row in response.css('table > tr'):
            genre = row.css('td.note a::text').get()
            
            if genre:
                yield { 'genre': genre }
