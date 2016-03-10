from crawler.utils.moduleimport import *
import re
import urllib

'''
Function: remove custom attrs in hml
'''


def remove_tags(html):
    # Allow attrs
    allow_attrs = ['src', 'href']
    cleaner = clean.Cleaner(safe_attrs_only=True,
                            safe_attrs=frozenset(allow_attrs))
    results = cleaner.clean_html(html)
    return results


'''
Function: add base_url to url if short url and skip if url is full url
'''


def add_base_url_to_src(base_url, input_html):
    data_output = []
    data_input = re.findall("src=\"(/\\w+/[^\"]+)", input_html)
    for data in data_input:
        if data.startswith("http"):
            data_output.append(data)
        else:
            data_output.append(base_url + data)
    return data_output


'''
Function: check url exists
'''


def check_url_use(input_url):
    check_var = urllib.urlopen(input_url).getcode()
    if check_var == 200:
        return True
    else:
        return False
