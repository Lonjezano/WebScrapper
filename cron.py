from scrapy.crawler import CrawlerProcess
from VacancyWebsite.crawler.crawler.spiders.vacancy import NyasaSpider, Mw24Spider, VacancySpider
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings


def crawl():
    import os
    cw = os.getcwd()
    path = '/crawler'
    ourPath = cw + os.path.join(path)

    if (ourPath):
        os.chdir(ourPath)
        os.system('scrapy crawl vacancy')

crawl()


