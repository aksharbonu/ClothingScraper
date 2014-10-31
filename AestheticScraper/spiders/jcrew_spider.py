# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from tutorial.items import ClothingItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class JCrewSpider(CrawlSpider):
    name = "jcrew"
    allowed_domains = ["jcrew.com"]
    start_urls = [
        "https://www.jcrew.com/mens_category/shirts.jsp"
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
    Rule(LinkExtractor(allow=(r'.*/mens_.*/(\d\d\d\d\d|\w\d\d\d\d).*', ), deny=()), callback = "parse_clothing_item", follow = True),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
    Rule(LinkExtractor(allow=()),),
    )


    def parse_clothing_item(self, response):
        item = ClothingItem()
        #add _3x_zoom to end
        smallimage = response.xpath('//img[contains(@class, "prod-main-image")]/@src').extract()
        item['image'] = [smallimage[0][:-1] + "_3x_zoom" + smallimage[0][-1:]]
        item['price'] = response.xpath('//script/text()').re(r'e\',\'(\d+.\d+)')
        item['name'] = response.xpath('//meta[contains(@property, "og:title")]/@content').extract()
        yield item

