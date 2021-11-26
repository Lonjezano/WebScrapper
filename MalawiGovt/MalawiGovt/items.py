# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HackItem(scrapy.Item):
    data = scrapy.Field()


class MalawigovtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    vacancy_title = scrapy.Field()
    vacancy_link = scrapy.Field()
    vacancy_expiry = scrapy.Field()
    bwb_tender = scrapy.Field()
    job_name = scrapy.Field()
    job_company = scrapy.Field()
    job_status = scrapy.Field()
    job_place = scrapy.Field()
    job_description = scrapy.Field()
    job_link = scrapy.Field()

    pass
