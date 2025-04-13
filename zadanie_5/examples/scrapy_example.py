import scrapy
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            print(f"{text} — {author}")

# Uruchomienie bez tworzenia projektu scrapy
process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()
