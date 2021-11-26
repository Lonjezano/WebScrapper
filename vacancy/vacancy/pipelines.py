# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class VacancyPipeline:

    def __init__(self):
        # self.create_connection()
        # self.create_table()
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn['vacancy']
        self.collection = db['vacancy_tb']


    def process_item(self, item, spider):
        # self.store_db(item)
        self.collection.insert(dict(item))

        return item
