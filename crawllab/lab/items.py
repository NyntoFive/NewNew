# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

from dataclasses import dataclass
from typing import Optional, Any, Callable, Iterable, Union

from pydantic import BaseModel, HttpUrl, condecimal

from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst, MapCompose

import re
import json


def remove_tabs_and_html(value):
    return remove_tags(value.replace('\r\n\t','\n').replace('\t','').replace('/r/n',''))

def remove_symbols(value):
    if isinstance(value, str):
        return value.replace('$','')
    else:
        return str(value.replace("$",''))


def fix_urls(value, base_url="https://knifekits.com/vcom/"):
    if not value.startswith(base_url):
        return base_url + value

class Data(scrapy.Item):
    link = scrapy.Field(output_processor=TakeFirst(), default=None)
    sku = scrapy.Field(output_processor=TakeFirst(), default=None)
    name = scrapy.Field(output_processor=TakeFirst(), default=None)
    main_image = scrapy.Field(input_processor=MapCompose(fix_urls), output_processor=TakeFirst(), default=None)
    products_id = scrapy.Field(output_processor=TakeFirst(), default=None)
    title = scrapy.Field(output_processor=TakeFirst(), default=None)
    keywords = scrapy.Field(output_processor=TakeFirst(), default=None)
    short_desc = scrapy.Field(output_processor=TakeFirst(), default=None)
    price = scrapy.Field(input_processor=MapCompose(remove_symbols), output_processor=TakeFirst(), default=0)
    description = scrapy.Field(
        input_processor=MapCompose(remove_tabs_and_html),
        default=None
    )
    manufacturer = scrapy.Field(output_processor=TakeFirst(), default=None)
    image_urls = scrapy.Field(default=None)
    breadcrumbs = scrapy.Field(default=None)
    discount_tiers = scrapy.Field(input_processor=MapCompose(remove_symbols), default=None)
    discount_amount = scrapy.Field(default=None)

@dataclass
class DataItem:
    """ spider crawly.py
    """
    link: HttpUrl
    sku: str
    name: Optional[str] = None
    main_image: Optional[HttpUrl] = None
    products_id: Optional[int] = None
    title: Optional[str] = None
    keywords: Optional[str] = None
    short_desc: Optional[str] = None
    price: Optional[str] = 0
    description: Optional[str] = None
    cleaned_description: Optional[str] = None
    manufacturer: Optional[str] = None
    
    image_urls: Optional[str] = None
    breadcrumbs: Optional[str] = None
    discount_tiers: Optional[str] = None
    discount_amount: Optional[str] = None

def read_data(file="dj/pages/scripts/recent.json"):
    with open(file) as f:
        data = json.load(f)
    return data


