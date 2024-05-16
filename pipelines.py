# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import csv


class ImgparserPipeline:
    def __init__(self):
        self.writer = csv.writer(open('img_unsplash.csv', 'a', newline='', encoding='utf-8'))
        self.writer.writerow(['url', 'path', 'name', 'category'])

    def process_item(self, item, spider):
        self.writer.writerow([item['url'], item['image'].get('path'), item['name'], item.get('category', 'no category')])
        return item


class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        try:
            yield scrapy.Request(item['image'])
        except Exception as e:
            print(e)

    def item_completed(self, results, item, info):
        if results:
            item['image'] = results[0][1] if results[0][0] else None
        return item