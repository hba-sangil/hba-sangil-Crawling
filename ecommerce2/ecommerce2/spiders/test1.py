import scrapy
from ecommerce2.items import Ecommerce2Item

class Test1Spider(scrapy.Spider):
    name = "test1"
    start_urls = ["https://www.gmarket.co.kr/n/best",
    "https://www.gmarket.co.kr/n/superdeal"]

    #크롤링 부분
    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()
        for title in titles:
            item = Ecommerce2Item() #추출할 데이터를 위한 객체 생성
            item['title'] = title
            yield item