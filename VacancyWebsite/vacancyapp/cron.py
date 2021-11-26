from scrapy.crawler import CrawlerProcess
from crawler.crawler.spiders.vacancy import NyasaSpider, NationSpider,Mw24Spider, VacancySpider
from scrapy.settings import Settings
from crawler.crawler import settings as my_settings


def crawl():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(VacancySpider)
    process.crawl(NyasaSpider)
    # process.crawl(Mw24Spider)
    process.crawl(NationSpider)
    process.start()




