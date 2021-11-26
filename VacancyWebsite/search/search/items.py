# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from vacancyapp.models import ScrappedData, ScrappedVacancy, ScrappedTender, ScrappedAdvert, ScrappedNew


class ScraperItem(DjangoItem):
    django_model = ScrappedData


class VacancyItem(DjangoItem):
    django_model = ScrappedVacancy


class TenderItem(DjangoItem):
    django_model = ScrappedTender


class AdvertItem(DjangoItem):
    django_model = ScrappedAdvert


class NewsItem(DjangoItem):
    django_model = ScrappedNew


class TestItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    date = scrapy.Field()
