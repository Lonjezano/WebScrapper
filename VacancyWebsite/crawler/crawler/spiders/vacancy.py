import scrapy
from ..items import ScraperItem, VacancyItem, TenderItem, AdvertItem, NewsItem, TestItem
from vacancyapp.models import ScrappedData, ScrappedVacancy, ScrappedTender, ScrappedAdvert, ScrappedNew
from datetime import datetime


class VacancySpider(scrapy.Spider):
    name = "vacancy"
    start_urls = ['https://www.myjobo.com/jobs']

    def parse(self, response, **kwargs):
        all_jobs = response.css(".searchList li")
        now = datetime.now()

        for index, job in enumerate(all_jobs):
            items = ScraperItem()

            job_name = response.css("h3 a::text")[index].extract()
            job_company = job.css("li:nth-child(3) .companyName a , .companyName+ .companyName a"). \
                css('::text').extract_first()
            job_status = job.css(".fulltime::text").extract_first()
            job_place = job.css(".location span::text").extract_first()
            job_description = job.css("p::text").extract_first()
            job_link = job.css(".listbtn a::attr(href)").extract_first()

            if ScrappedData.objects.filter(name=job_name).exists():
                continue

            items['name'] = job_name
            items['company'] = job_company
            items['status'] = job_status
            items['type'] = 'vacancy'
            items['location'] = job_place
            items['description'] = job_description
            items['link'] = job_link
            items['date'] = now.strftime("%Y-%m-%d")

            yield items

        next_page = response.css('.page-item:nth-child(13) .page-link').css("::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class ESCOMSpider(scrapy.Spider):
    name = 'escom'
    start_urls = ["http://www.escom.mw/tender-documents.php"]

    def parse(self, response, **kwargs):
        all_tenders = response.xpath("//tr")

        for index, tender in enumerate(all_tenders, start=1):
            item = ScraperItem()

            tender_name = response.css(f'tr:nth-child({index}) a::text').extract_first()
            tender_description = response.css(f'tr:nth-child({index}) td:nth-child(3)').css("::text").extract_first()
            tender_date = response.css(f"tr:nth-child({index}) td:nth-child(4)::text").extract_first()

            item['name'] = tender_name
            item['company'] = 'ESCOM'
            item['description'] = tender_description
            item['type'] = 'tender'
            item['location'] = tender_date

            yield item


class BWBSpider(scrapy.Spider):
    name = 'bwb'
    start_urls = ['https://bwb.mw/Tenders.php']

    def parse(self, response, **kwargs):
        import re
        all_tenders = response.css('#page-container li')
        now = datetime.now()

        for index, tender in enumerate(all_tenders, start=1):
            if not index % 2 == 0:
                item = TenderItem()

                tender_name = response.css(f'li:nth-child({index})::text').extract_first()
                tender_link = response.css(f'li:nth-child({index})::attr(onclick)').extract_first()
                pdf_link = re.findall("'([^']*)'", tender_link)
                actual_link = f"https://bwb.mw/{pdf_link[0]}"

                item['name'] = tender_name
                item['company'] = "Blantyre Waterboard"
                item['link'] = actual_link
                item['scrapped_date'] = now.strftime("%Y-%m-%d")

                yield item


class MRASpider(scrapy.Spider):
    name = "mra"
    start_urls = [
        'https://www.mra.mw/tenders'
    ]

    def parse(self, response, **kwargs):
        all_tenders = response.css('.clearfix dt')
        now = datetime.now()

        for index, tender in enumerate(all_tenders):
            item = TenderItem()

            tender_name = response.css(f'dt:nth-child({index}) a::text').extract_first()

            item['name'] = tender_name
            item['company'] = 'Malawi Revenue Authority'
            item['link'] = response.css(f'dt:nth-child({index}) a::attr(href)').extract_first()
            item['scrapped_date'] = now.strftime("%Y-%m-%d")

            yield item


class ProcurementSpider(scrapy.Spider):
    name = 'procurement'
    start_urls = ['https://www.ppda.mw/ppda/procurementnoticesdisplayweb.php']

    def parse(self, response, **kwargs):
        import re
        all_tenders = response.xpath('//tr')
        now = datetime.now()

        for index, tender in enumerate(all_tenders, start=1):
            if not index % 2 == 0:
                item = TenderItem()

                tender_name = response.css(f'tr:nth-child({index}) td:nth-child(1)::text').extract_first()
                tender_company = response.css(f'tr:nth-child({index}) td:nth-child(2)::text').extract_first()
                tender_date = response.css(f'tr:nth-child({index}) td:nth-child(4)::text').extract_first()
                tender_link = response.css(f'tr:nth-child({index}) td:nth-child(5) a::attr(href)').extract_first()
                actual_link = f"https://www.ppda.mw/ppda/{tender_link}"

                item['name'] = tender_name
                item['company'] = tender_company
                item['link'] = actual_link
                item['close_date'] = tender_date
                item['scrapped_date'] = now.strftime("%Y-%m-%d")

                yield item


class ReserveSpider(scrapy.Spider):
    name = 'rbm'
    start_urls = ['http://www.rbm.mw/MediaCenter/Adverts/']

    def parse(self, response, **kwargs):
        all_adverts = response.xpath('//*[(@id = "ContentListTable")]//tbody//tr')
        now = datetime.now()

        for index, advert in enumerate(all_adverts, start=1):
            item = AdvertItem()

            advert_name = response.css(f'tr:nth-child({index}) a::text').extract_first()
            advert_link = response.css(f'tr:nth-child({index}) a::attr(href)').extract_first()
            advert_date = response.css(f"tr:nth-child({index}) td+ td::text").extract_first()

            item['name'] = advert_name
            item['company'] = "Reserve Bank of Malawi"
            item['link'] = f'http://www.rbm.mw/{advert_link}'
            item['posted_date'] = advert_date
            item['scrapped_date'] = now.strftime("%Y-%m-%d")

            yield item


class NyasaSpider(scrapy.Spider):
    name = "nyasa"
    start_urls = ["https://www.nyasatimes.com"]

    def parse(self, response):
        data = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "extra-option-li", " " ))]')

        for line in data:
            link = line.xpath(".//a/@href").extract_first()
            yield scrapy.Request(url=link, callback=self.parse_attr)

    def parse_attr(self, response):
        item = NewsItem()

        now = datetime.now()
        text = response.css(".nyasa-content p:nth-child(1)::text").extract_first()
        title = response.css(".nyasa-title::text").extract_first()
        image = response.css(".nyasa-content figure img::attr(src)").extract()[4]
        posted_date = response.xpath('//span[@class="glyphicon glyphicon-calendar"]/following-sibling::text()').get()

        if ScrappedNew.objects.filter(title=title).exists():
            pass

        else:
            item['title'] = title
            item['site'] = 'nyasatimes'
            item['description'] = text
            item['image_link'] = image
            item['link'] = response.url
            item['posted_date'] = posted_date
            item['scrapped_date'] = now.strftime("%Y-%m-%d")

            yield item


class Mw24Spider(scrapy.Spider):
    name = 'malawi24'
    start_urls = ['https://malawi24.com/category/top-news/']

    def parse(self, response, **kwargs):
        all_adverts = response.xpath('//*[(@id = "ContentListTable")]//tbody//tr')
        now = datetime.now()

        for index, advert in enumerate(all_adverts, start=1):
            item = NewsItem()

            now = datetime.now()
            text = response.css(".nyasa-content p:nth-child(1)::text").extract_first()
            title = response.css(".nyasa-title::text").extract_first()
            image = response.css(".nyasa-content figure img::attr(src)").extract()[4]
            posted_date = response.xpath('//span[@class="glyphicon glyphicon-calendar"]/following-sibling::text()').get

            item['title'] = title
            item['site'] = 'nyasatimes'
            item['description'] = text
            item['image_link'] = image
            item['posted_date'] = posted_date
            item['scrapped_date'] = now.strftime("%Y-%m-%d")

            yield item


class NationSpider(scrapy.Spider):
    name = 'nation'
    start_urls = ['https://www.mwnation.com/section/news/national-news/']

    def parse(self, response, **kwargs):
        all_news = response.xpath('///*[contains(concat( " ", @class, " " ), concat( " ", "jeg_pl_md_1", " " ))]')

        for index, news in enumerate(all_news, start=1):
            item = NewsItem()
            now = datetime.now()
            text = response.css(f".jeg_pl_md_1:nth-child({index}) p::text").extract_first()
            title = response.css(f".jeg_pl_md_1:nth-child({index}) .jeg_post_title a::text").extract_first()
            image = response.css(f".jeg_pl_md_1:nth-child({index}) .wp-post-image").css("::attr(data-src)").extract_first()
            link = news.css(f".jeg_pl_md_1:nth-child({index}) .jeg_post_title a::attr(href)").extract_first()
            posted_date = news.css(f'.jeg_pl_md_1:nth-child({index}) .jeg_meta_date a::text').extract_first()

            if ScrappedNew.objects.filter(title=title).exists():
                pass

            else:
                item['title'] = title
                item['site'] = 'The nation'
                item['description'] = text
                item['image_link'] = image
                item['link'] = link
                item['posted_date'] = posted_date
                item['scrapped_date'] = now.strftime("%Y-%m-%d")

                yield item
