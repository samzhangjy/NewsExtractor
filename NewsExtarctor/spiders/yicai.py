from typing import List
import scrapy
import json


class YicaiSpider(scrapy.Spider):
    name = 'yicai'
    allowed_domains = ['www.yicai.com']
    start_urls = ['https://www.yicai.com/news/101020017.html']

    def parse(self, response):
        text__: List[str] = response.css('.m-txt').css('::text').extract()
        title: str = response.css('title::text').extract()[0]
        result: str = ''
        for __ in text__:
            t = __.replace('\r', '').replace('\n', '').strip()
            if t != '':
                result += t
        with open(f'./res/{title}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                'title': title,
                'content': result
            }, ensure_ascii=False, indent=2))
