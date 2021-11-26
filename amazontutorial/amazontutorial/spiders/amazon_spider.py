import scrapy
from ..items import AmazontutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1616101414&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0'
    ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        product_author = response.css(".sg-col-12-of-20 .sg-col-12-of-20 .a-size-base+ .a-size-base").css("::text").extract()
        product_price = response.css(".a-spacing-top-small .a-price-whole").css("::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
