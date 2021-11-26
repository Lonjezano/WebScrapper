import scrapy
from scrapy.http import FormRequest
from ..items import VacancyItem


class VacancySpider(scrapy.Spider):
    name = "vacancy"
    start_urls = {
        'http://quotes.toscrape.com/login'
    }

    def parse(self, response, **kwargs):
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'lonjezano',
            'password': '123456'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
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



