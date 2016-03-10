# -*- coding: utf-8 -*-
from crawler.utils.moduleimport import *


class WebSpider(CrawlSpider):
    name = "web"
    cpt = 0

    def __init__(self, config_file=None, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        if config_file is not None:
            self.data_config = json.load(open(config_file))
        self.start_urls = self.data_config['start_urls']
        self.base_url = self.data_config['base_url']

        if self.data_config['rules']:
            # Get object rules from config file
            WebSpider.rules = [eval(rule) for rule in self.data_config['rules']]
            # Recompile the Rules
            super(WebSpider, self)._compile_rules()

    def parse_product(self, response):
        if self.data_config is not None:
            print self.cpt
            print response.url
            item = CrawlerItem()
            fields_config = self.data_config['fields']

            for key in fields_config.keys():
                try:
                    xpath_config = fields_config[key]['xpath']
                    re_config = fields_config[key].get('re')
                    python_config = fields_config[key].get('python')

                    item[key] = WebSpider.extract_data(self, response, key, xpath_config, re_config, python_config)

                except Exception as e:
                    print e
                    item[key] = fields_config[key]
            item['product_url'] = response.url
            try:
                item['product_name'] = fields_config['product_name']
            except Exception as e:
                print e
                print "Missing field 'product_name' on config input file! Please Check!"
            yield item

    # Extract data
    @staticmethod
    def extract_data(self, response, key, xpath_config, re_config, python_config):
        data = None
        if isinstance(xpath_config, unicode):
            try:
                xpath_config = xpath_config.encode('utf-8', 'ignore')
                if re_config:
                    data = response.xpath(xpath_config).re(re_config)
                else:
                    data = response.xpath(xpath_config).extract()
            except Exception as e:
                print e

        elif isinstance(xpath_config, list):

            data = []
            for xpath_c in xpath_config:
                if re_config:
                    ele = response.xpath(xpath_c).re(re_config)
                    if isinstance(ele, str):
                        data.append(ele)
                    elif isinstance(ele, list):
                        data += ele
                else:
                    ele = response.xpath(xpath_c).extract()
                    data += ele

        if isinstance(python_config, unicode):
            data = eval(python_config.encode('utf-8', 'ignore'))

        if key == 'description':
            return FormatData.description(self=self, input_value=data)
        if key == 'title':
            return FormatData.title(self=self, input_value=data)
        elif key == 'image_urls':
            return FormatData.image_urls(self=self, input_value=data)
        elif key == 'post_date':
            return FormatData.post_date(self=self, input_value=data)
        elif key == 'categories':
            return FormatData.categories(self=self, input_value=data)
        elif key == 'tags':
            return FormatData.tags(self=self, input_value=data)
        elif key == 'description_urls':
            return FormatData.description_url(self=self, input_value=data)
        else:
            return data
