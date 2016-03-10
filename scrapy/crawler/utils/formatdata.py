from crawler.utils.html_string import *
import re


class FormatData:
    def __init__(self):
        pass

    '''
    Function: Format description field
    '''

    @staticmethod
    def description(self, input_value):

        html_desc = None
        html_desc_list = []
        if isinstance(input_value, list):
            for input_v in input_value:
                html_desc_list.append(remove_tags(input_v))
                html_desc = ' '.join(html_desc_list)

            # Replace short url by full url
            short_src_url_ = re.findall("src=\"(/\\w+/[^\"]+)", html_desc)
            full_src_url = add_base_url_to_src(
                base_url=self.base_url, input_html=html_desc)

            if len(short_src_url_) > 0:
                for i in short_src_url_:
                    for j in full_src_url:
                        if i in j:
                            # check url exist
                            if check_url_use(j):
                                html_desc = html_desc.replace(i, j)

            return html_desc

        elif isinstance(input_value, unicode):
            return remove_tags(input_value)

    '''
    Function: Format description_url field
    '''

    @staticmethod
    def description_url(self, input_value):
        results = []
        if isinstance(input_value, list):
            for url in input_value:
                url = url.encode('utf-8', 'ignore')
                if url.startswith('http'):
                    # check url exist
                    if check_url_use(input_url=url):
                        results.append(url)
                else:
                    full_url = self.base_url + url
                    # check url exist
                    if check_url_use(input_url=full_url):
                        results.append(full_url)

            return '; '.join(results)

    '''
    Function: Format title field
    '''

    @staticmethod
    def title(self, input_value):
        if isinstance(input_value, list):
            return input_value[0]

    '''
    Function: Format post_date field
    '''

    @staticmethod
    def post_date(self, input_value):
        if isinstance(input_value, list):
            return input_value[0]

    '''
    Function: Format image_urls field
    '''

    @staticmethod
    def image_urls(self, input_value):
        results = []
        if isinstance(input_value, list):
            for url in input_value:
                url = url.encode('utf-8', 'ignore')
                if url.startswith('http'):
                    # check url exist
                    if check_url_use(url):
                        results.append(url)
                else:
                    full_url = self.base_url + url
                    # check url exist
                    if check_url_use(input_url=full_url):
                        results.append(full_url)

        return '; '.join(results)

    '''
    Function: Format categories field
    '''

    @staticmethod
    def categories(self, input_value):
        if isinstance(input_value, list):
            return '; '.join(input_value)

    '''
    Function: Format tags field
    '''

    @staticmethod
    def tags(self, input_value):
        if isinstance(input_value, list):
            return '; '.join(input_value)
