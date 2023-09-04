import scrapy
from scrapy.spiders import CrawlSpider
import logging

class CKKCrawler(CrawlSpider):
    name = "crawler"
    allowed_domains = ["knifekits.com"]
    start_urls = ['https://knifekits.com/vcom/nife-making-kitsblades-c-1070.html',
                  'https://knifekits.com/vcom/knife-making-handles-c-40.html',
                  'https://knifekits.com/vcom/knife-making-parts-c-60.html',
                  'https://knifekits.com/vcom/knife-making-steel-c-46.html',
                  'https://knifekits.com/vcom/knife-making-tools-c-49.html',
                  'https://knifekits.com/vcom/knife-making-carrydisplay-c-515.html',
                  'https://knifekits.com/vcom/knife-making-training-c-59.html',
                  'https://knifekits.com/vcom/holster-making-materials-c-1071.html',
                  'https://knifekits.com/vcom/holster-making-mountings-c-56.html',
                  'https://knifekits.com/vcom/holster-making-parts-c-1074.html',
                  'https://knifekits.com/vcom/holster-making-tools-c-1072.html',
                  'https://knifekits.com/vcom/holster-making-gun-molds-c-585.html',
                  'https://knifekits.com/vcom/holster-making-combo-kits-c-589.html',
                  'https://knifekits.com/vcom/holster-making-shells-c-993.html',
                  'https://knifekits.com/vcom/lanyard-making-supplies-c-61.html',
                  'https://knifekits.com/vcom/hobby-kits-assorted-c-332.html',
                  'https://knifekits.com/vcom/more-knife-accessories-c-1068_42.html',
                  'https://knifekits.com/vcom/more-knives-for-sale-c-1068_445.html',
                  'https://knifekits.com/vcom/more-apparelclothing-c-1068_460.html',
                  'https://knifekits.com/vcom/more-workbench-c-1068_212.html',
                  'https://knifekits.com/vcom/more-apparelclothing-c-1068_460.html',
                  'https://knifekits.com/vcom/more-boneyard-specials-c-1068_532.html']

