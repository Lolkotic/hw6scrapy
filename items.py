# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose


def proccess_category(value):
    return ', '.join(value)


def proccess_name(value):
    if value:
        return value[0].strip()
    return 'noname'


def proccess_images(value):
    return value.split(',')[0].split()[0]


class ImgparserItem(scrapy.Item):
    category = scrapy.Field(input_processor=Compose(proccess_category), output_processor=TakeFirst())
    name = scrapy.Field(input_processor=Compose(proccess_name), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    image = scrapy.Field(input_processor=MapCompose(proccess_images), output_processor=TakeFirst())
    _id = scrapy.Field()