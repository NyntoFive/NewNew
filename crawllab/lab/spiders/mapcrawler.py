from datetime import datetime
from scrapy.spiders import SitemapSpider


class FilteredSitemapSpider(SitemapSpider):
    name = "filtered_sitemap_spider"
    allowed_domains = ["knifekits.com", "holstersmith.com"]
    sitemap_urls = ["https://knifekits.com/vcom/smproducts.xml",
                    "https://holstersmith.com/vcom/smproducts.xml"]
    
    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry["lastmod"], "%Y-%m-%d")
            if date_time.year >= 2023:
                yield entry
