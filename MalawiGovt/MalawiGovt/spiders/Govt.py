import scrapy
from ..items import MalawigovtItem, HackItem


class GovtSpider(scrapy.Spider):
    name = 'Govt'
    start_urls = ['http://www.escom.mw/careers.php', 'https://www.bwb.mw/Tenders.php']

    def parse(self, response):
        items = MalawigovtItem()

        container = response.css(".default")

        for data in container:
            vacancy_title = data.css(".default a::text").extract()
            vacancy_link = data.css(".default a::attr(href)").get()
            vacancy_expiry = data.css(".news_dhate span::text").extract()


            items['vacancy_title'] = vacancy_title
            items['vacancy_link'] = f"http://www.escom.mw/{vacancy_link}"
            items['vacancy_expiry'] = vacancy_expiry

            yield items

        tender_lwb = response.css("#page-container li::text").extract()
        yield {"tender_lwb": tender_lwb}


class WaterSpider(scrapy.Spider):
    name = 'bwb'
    start_urls = ['https://www.bwb.mw/Tenders.php']

    def parse(self, response):
        items = MalawigovtItem()

        container = response.css(".col-md-12+ .col")

        for data in container:
            tender_lwb = response.css("#page-container li::text").extract()
            items['bwb_tender'] = tender_lwb
            yield items


class JobSpider(scrapy.Spider):
    name = 'rbm'
    start_urls = ['http://www.rbm.mw/MediaCenter/Adverts/']

    def parse(self, response, **kwargs):
        item = MalawigovtItem()
        all_adverts = response.xpath('//*[(@id = "ContentListTable")]//tbody//tr')

        for index, advert in enumerate(all_adverts, start=1):
            advert_name = response.css(f'tr:nth-child({index}) a::text').extract_first()
            advert_date = advert.css(f"tr:nth-child({index}) td+ td::text").extract_first()

            item['job_name'] = advert_name
            item['job_place'] = advert_date

            yield item


