import scrapy
from requests_html import HTML, HTMLSession
# import arrow
# from ..items import CKKItem

# sys.path.append(os.path.dirname(os.path.abspath('.')))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# import django
# django.setup()

def read_local_sitemap(file='../smproducts.xml'):
    ## Reads local file, parses into a list of (Url, last_modified) tuples
    with open(file) as f:
        txt = f.read()
        page = HTML(html=txt)
    urls, timestamps = page.xpath('//loc/text()'), page.xpath('//lastmod/text()')
    return list(zip(urls,timestamps))

def find_start_urls(url="https://knifekits.com/vcom/smproducts.xml"):
    session = HTMLSession()
    page = session.get(url)
    return list(zip(page.html.xpath('//loc/text()'), page.html.xpath('//lastmod/text()')))

    
    
    
    


class KnifekitsSpider(scrapy.Spider):
    name = 'kk'
    allowed_domains = ['knifekits.com', 'holstersmith.com']
    custom_settings = {
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        'LOG_FILE': 'log.txt'
    }
    
    # response.xpath('//a[contains(@href, "image")]/text()').re(r"Name:\s*(.*)")
    
    start_urls = [
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-1375-1450-p-22069.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-125-1575-p-22067.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-115-175-950-p-22088.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-115-175-1025-p-22087.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-115-1500-p-22089.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-9875-p-22079.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-1875-p-22086.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-1875-130-p-22078.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-168-550-p-22085.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-150-650-p-22084.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-150-12375-p-22080.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-1375-110-p-22082.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-1375-110-p-22081.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-110-1312-1025-p-22083.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-225-p-22057.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-750-p-22056.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-750-p-22053.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-1875-725-p-22055.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-1812-525-p-22051.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-175-750-p-22054.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-1625-650-p-22052.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-150-130-p-22068.html',
        'https://www.knifekits.com/vcom/usa-carbon-damascus-416-layer-521005160203e15n20-100-150-130-p-22065.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-substrate-salisbury-infused-080-8in-12in-p-22127.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-hexcam-5echo-micro-infused-080-8in-12in-p-22121.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-dutch-woodland-infused-080-8in-12in-p-22118.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-the-mountain-viper-infused-080-8in-12in-p-22125.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-substrate-salisbury-infused-080-12in-12in-p-22095.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-hexcam-5echo-micro-infused-080-12in-12in-p-22092.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-dutch-woodland-infused-080-12in-12in-p-22100.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-the-mountain-viper-infused-080-12in-12in-p-22097.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-hexcam-wasteland-micro-infused-080-8in-12in-p-22122.html',
        'https://www.knifekits.com/vcom/holstex-sheet-basketweave-hexcam-wasteland-micro-infused-080-12in-12in-p-22093.html',
    ]
    
    # start_urls = get_updated_urls(load_file())   #### Crawl updated urls from the past 7 days
    # start_urls = [i[0] for i in load_urls()]                                                   #### Crawl all urls
    def parse(self, response):
        base_url = "https://" + response.url.split('/')[2]+"/vcom/"
        item = {}
        item["link"] = response.xpath('//*[@rel="canonical"]/@href').get()
        item["sku"] = response.xpath('//span[@itemprop="model"]/descendant-or-self::text()').get()
        item["name"] = response.xpath('//h1/descendant::span[@itemprop="name"]/text()').get()
        item["main_image"] = response.xpath('//div[@class="piGalMain"]/img/@src').get()
        item["products_id"] = response.xpath('//input[@name="products_id"]/@value').get()
        item["title"] = response.xpath("/html/head/title/text()").get()
        item["keywords"] = response.xpath('.//meta[@name="keywords"]/@content').get()
        item["short_desc"] = response.xpath('//meta[@name="description"]/@content').get()
        item["price"] = response.xpath('.//*[@itemprop="price"]/text()').get().replace('$','')
        item["description"] = response.xpath('//div[@itemprop="description"]').get()
        item['manufacturer'] = response.xpath('//*[@itemprop="manufacturer"]/meta/@content').get()
        image_urls = [base_url+img for img in response.xpath('//*[@class="thumbnail"]/@data-image').getall()]
        bcrumbs = response.xpath('.//*[@class="breadcrumb"]/descendant-or-self::text()').getall()
        discount_tiers=response.xpath('.//*[@class="DiscountPriceQty"]/descendant-or-self::text()').getall()
        discount_amount=response.xpath('.//*[@class="DiscountPrice"]/descendant-or-self::text()').getall()
        item['image_urls'] = image_urls
        item['breadcrumbs'] = bcrumbs[::2]
        if len(discount_amount) >= 1 or len(discount_tiers) >= 1:
            item['discount_tiers'] = discount_tiers
            item['discount_amount'] = discount_amount
        if item['main_image'].startswith('images/'):
            item['main_image']=base_url + item['main_image']
        yield item

# class HolstersmithSpider(scrapy.Spider):
#     name = 'hs'
#     allowed_domains = ['knifekits.com', 'holstersmith.com']
#     start_urls=[]
#     # start_urls = get_updated_urls(load_urls("https://holstersmith.com/vcom/smproducts.xml"))   #### Crawl updated urls from the past 7 days
#     # start_urls = [i[0] for i in load_urls()]                                                   #### Crawl all urls
    
#     def parse(self, response):
#         item={}
#         for k,v in fields.items():
#             item[k] = response.xpath(v).get()
#         for k,v in list_fields.items():
#             item[k] = response.xpath(v).getall()
#         base_url = "https://" + response.url.split('/')[2]+"/vcom/"
#         item['image_urls'] = ["https://" + response.url.split('/')[2]+"/vcom/" + img for img in item['image_urls']]
#         item['main_image'] = base_url + item['main_image']
#         if "$" in item['price']:
#             item['price'] = item['price'].replace('$','')
#         if "Home" in item['breadcrumbs'][0]:
#             item['breadcrumbs'] = item['breadcrumbs'][4::2]
#         item['description'] = {"html": clean_description(item['description']), "text": remove_html("\n".join(clean_description(item['description'])))}
#         if len(item['discount_amount'])>=1 and "$" in item['discount_amount'][0]:
#             item['discount_amount'] =  [i.replace('$','').strip() for i in item['discount_amount']]

#         yield item
