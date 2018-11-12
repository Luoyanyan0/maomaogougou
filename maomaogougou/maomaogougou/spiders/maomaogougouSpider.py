import scrapy
from scrapy.spiders.crawl import CrawlSpider
from maomaogougou.items import MaomaogougouItem

class maomaogougou(scrapy.Spider):
    name = "maomaogougou"
    allowed_domains = ['maomaogougou.cn']
    start_urls = ['http://www.maomaogougou.cn/tupian/gougou/meng',
                  'http://www.maomaogougou.cn/tupian/maomi/gaoxiao']

    # 要爬取的图片URL规则
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    # 解析萌狗狗和搞笑猫页面，获得当前页面所有狗和猫的链接
    def parse(self, response):
        # 获取大标题   萌狗狗   搞笑猫咪
        big_dir = response.xpath("//strong/text()").extract()[0]
        pre = 'http://www.maomaogougou.cn'
        urls = response.xpath("//*[@id='list']/div[1]/div[@class='item']/a/@href").extract()
        if urls is not None:
            for url in urls:
                yield scrapy.Request(pre+url,
                callback= lambda response,big_dir_name=big_dir:self.detail(response,big_dir_name))

    # 在每一个标题的页面中获取标题，图片链接
    def detail(self, response,big_dir_name):
        item = MaomaogougouItem()
        name = response.xpath("//div[@class='title']/span/text()").extract_first()
        # name = response.xpath().
        url = response.xpath("//div[@id='pic']/img/@src").extract()
        item['img_title'] = name
        item['url'] = url
        item['big_dir_name'] = big_dir_name
        print(item['img_title'])
        print(item['url'])
        print(item['big_dir_name'])
        yield item


