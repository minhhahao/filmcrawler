from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lxml
from scrapy.contrib.spiders import CrawlSpider, Rule


class TestRuleSpider(CrawlSpider):
    name = "rules"
    start_urls = ["http://thuthuatphanmem.vn/"]
    cpt = 0
    rules = [
        Rule(lxml(allow=('.*'), restrict_xpaths=("//h2[@class='title']/a")), callback='parse_product'),
        Rule(lxml(allow=('.*'), restrict_xpaths=("//ul[@class='pagination']/li/a")), follow=True)
    ]

    def parse_product(self, response):
        self.cpt += 1
        print self.cpt
        print response.url
        # print self.cpt
        return None

    def passCat(self, response):
        print "passFollows------------------"
        self.cpt += 1
        print self.cpt
        print response.url
        return None
