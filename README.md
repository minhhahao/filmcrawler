# Crawl Film data
```
Scrapy FilmCrawler Project Readme
```

```
Create Environment run scrapy
```
Using virtualenv.
Install virtualenv: $pip install virtualenv
Create environment: $virtualenv env_linux (with env_linux is name virtualenv created in Linux machine)

```
Activate virtualenv
```
Activate virtualenv on Linux/Mac OS: $source env_linux/bin/activate
Activate virtualenv on Windows     : >. env_linux\Script\activate
Result after activate: (env_linux)$

```
Install Scrapy
```
Install scrapy on virtualenv: (env_linux)$pip install -r requirement.txt


```
Run Scrapy
```
Run scrapy: $scrapy crawl web -a config_fil=sources/config/<name_config_file> -o output/<name_output_file>
Example: $scrapy crawl web -a config_file=sources/config/baoboi_config.json -o output/baobao_output.json

```
Deactivate virtualenv
```
Deactivate virtualenv: $deactivate
