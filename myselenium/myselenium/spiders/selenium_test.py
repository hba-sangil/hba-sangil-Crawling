import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class SeleniumTestSpider(scrapy.Spider):
    name = "selenium_test"
    allowed_domains = ["davelee-fun.github.io/blog/TEST/index.html"]
    start_urls = ["https://davelee-fun.github.io/blog/TEST/index.html"]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(2)
        id_ = self.driver.find_element(By.CSS_SELECTOR, '#username')
        pw_ = self.driver.find_element(By.CSS_SELECTOR, '#password')
        id_.send_keys('abcd@abcd.com')
        time.sleep(2)
        pw_.send_keys('abcd')
        time.sleep(2)

        submit = self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        data = self.driver.find_element(By.XPATH, '//div[@class="message"]')
        print(data.text)
        self.driver.quit()
        pass
