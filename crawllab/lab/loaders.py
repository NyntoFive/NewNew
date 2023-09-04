from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader
from w3lib import remove_tags

import re
import json


def remove_tags_and_html(value):
    return remove_tags(value.replace('\r\n','\n').replace('\t','').replace('/r/n',''))

def remove_symbols(value):
    if isinstance(value, str):
        return value.replace('$','')
    else:
        return str(value.replace("$",''))


def build_url(value, base_url="https://knifekits.com/vcom/"):
    if not value.startswith(base_url):
        return base_url + value

class CKKLoader(ItemLoader):
    default_output_processor = TakeFirst()

    # link_in = MapCompose()
    # link_out = 
    # sku_in = MapCompose()
    # sku_out = 
    # name_in = MapCompose()
    # name_out = 
    main_image_in = MapCompose(build_url)
    main_image_out = TakeFirst()
    # products_id_in = 
    # products_id_out = 
    # title_in = MapCompose()
    # title_out = 
    # keywords_in = MapCompose()
    # keywords_out = 
    # short_desc_in = MapCompose()
    # short_desc_out = 
    price_in = MapCompose(remove_symbols)
    price_out = TakeFirst()
    description_in = MapCompose(remove_tags_and_html)
    description_out = TakeFirst()
    
    