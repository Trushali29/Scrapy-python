import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"
    # only web name on which spider will crawl
    allowed_domains = ["books.toscrape.com"]
    # can have multiple URLs
    start_urls = ["https://books.toscrape.com/"]
    # parse data responses from spider
   
    def parse(self, response):
        # to fetch all the data and store it in the csv or json file
        books = response.css('article.product_pod')
        for book in books:
            yield{
                'name' : book.css('h3 a::text').get(),
                'price' : book.css('div.product_price .price_color::text').get(),
                'url' : book.css('h3 a').attrib['href'],
            }


