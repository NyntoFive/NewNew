import scrapy
from requests_html import HTML, HTMLSession
from ..items import DataItem, Data

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from itemadapter import ItemAdapter
from w3lib.html import remove_tags

def find_start_urls(local_file="smproducts.xml"):
        with open(local_file) as f:
             txt = f.read()
             page = HTML(html=txt, )
             return list(zip(page.xpath('//loc/text()'), page.xpath('//lastmod/text()')))

class CKKSpider(scrapy.Spider):
    name = "ckk-detail"
    allowed_domains = ["knifekits.com", "holstersmith.com", "localhost"]
    start_urls = [url[0] for url in find_start_urls()]
#    start_urls = [
#         "https://www.knifekits.com/vcom/guard-floral-scroll-118-750-465-063-006-slot-nickel-silver-p-17429.html",
#         "https://www.holstersmith.com/vcom/monoblock-gear-clip-150-inch-wmounting-hardware-p-9494.html",
#         "https://www.knifekits.com/vcom/american-safety-molds-holster-molding-prop-for-fmk-9c1-prepped-p-21339.html",
#         "https://www.holstersmith.com/vcom/kydex-sheet-hot-pink-060-1ft-1ft-p-3112.html",
#         "https://www.knifekits.com/vcom/kydex-sheet-hunter-orange-060-1ft-1ft-p-3118.html",
#         "https://www.holstersmith.com/vcom/holstex-diy-thermoform-sheet-basketweavesmooth-desert-tan-080-8in-12in-p-8430.html",
#    ]


    def parse(self, response):
        loader = ItemLoader(item=Data(), response=response)
        loader.context['base_url'] = "https://" + response.url.split('/')[2]+"/vcom/"
        base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        loader.add_xpath("link", '//*[@rel="canonical"]/@href')
        loader.add_xpath("sku", '//span[@itemprop="model"]/descendant-or-self::text()')
        loader.add_xpath("name", '//h1/descendant::span[@itemprop="name"]/text()')
        loader.add_xpath("main_image", './/div[@class="piGalMain"]/img/@src')
        loader.add_xpath("products_id", '//input[@name="products_id"]/@value')
        loader.add_xpath("title", "/html/head/title/text()")
        loader.add_xpath("keywords", './/meta[@name="keywords"]/@content')
        loader.add_xpath("short_desc", '//meta[@name="description"]/@content')
        loader.add_xpath("price", './/*[@itemprop="price"]/text()')
        loader.add_xpath("description", '//div[@itemprop="description"]')
        loader.add_xpath('manufacturer', '//*[@itemprop="manufacturer"]/meta/@content')
        image_urls = [base_url+img for img in response.xpath('//*[@class="thumbnail"]/@data-image').getall()]
        bcrumbs = response.xpath('.//*[@class="breadcrumb"]/descendant-or-self::text()').getall()
        discount_tiers=response.xpath('.//*[@class="DiscountPriceQty"]/descendant-or-self::text()').getall()
        discount_amount=response.xpath('.//*[@class="DiscountPrice"]/descendant-or-self::text()').getall()
        loader.add_value('image_urls', image_urls)
        loader.add_value('breadcrumbs',bcrumbs[::2])
        if len(discount_amount) >= 1 or len(discount_tiers) >= 1:
            loader.add_value('discount_tiers', discount_tiers)
            loader.add_value('discount_amount', discount_amount)
        else:
            loader.add_value('discount_tiers', discount_tiers)
            loader.add_value('discount_amount', discount_amount)
        # if main_image.startswith('images/'):
            # item['main_image']=base_url + item['main_image']
        yield loader.load_item()
