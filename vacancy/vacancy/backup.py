import scrapy
from ..items import VacancyItem


class VacancySpider(scrapy.Spider):
    name = "vacancy"
    start_urls = {
        'http://quotes.toscrape.com/page/1/'
    }

    def parse(self, response, **kwargs):
        items = VacancyItem()

        all_div_quote = response.css("div.quote")

        for quote in all_div_quote:
            title = quote.css("span.text::text").extract()
            author = quote.css(".author::text").extract()
            tag = quote.css("a.tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

