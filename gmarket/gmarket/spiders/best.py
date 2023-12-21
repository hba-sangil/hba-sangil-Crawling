import scrapy
from gmarket.items import GmarketItem

class BestSpider(scrapy.Spider):
    name = "best"
    start_urls = ["https://www.gmarket.co.kr/n/best"]

    def parse(self, response):
        products = response.css('div.best-list li > a::text').getall()
        prices = response.css('div.best-list div.s-price > strong > span::text').getall()
        for product, price in zip(products, prices):
            item = GmarketItem()
            item['product'] = product
            item['price'] = price
            yield item