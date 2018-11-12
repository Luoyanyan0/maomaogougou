# -*- coding: utf-8 -*-
import random

BOT_NAME = 'maomaogougou'

SPIDER_MODULES = ['maomaogougou.spiders']
NEWSPIDER_MODULE = 'maomaogougou.spiders'


# 大多数情况下，网站都会根据我们的请求头信息来区分你是不是一个爬虫程序，如果一旦识别出这是一个爬虫程序，很容易就会拒绝我们的请求，
# 因此我们需要给我们的爬虫手动添加请求头信息，来模拟浏览器的行为，但是当我们需要大量的爬取某一个网站的时候，一直使用同一个User-Agent显然也是不够的，
# 因此，我们本节的内容就是学习在scrapy中设置随机的User-Agent。
#中文与客户端代理
# user_agent_list = [
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]

# UA = random.choice(user_agent_list)
# USER_AGENT = UA
# FEED_EXPORT_ENCODING = 'utf-8'


# robots.txt 是遵循 Robot协议 的一个文件，它保存在网站的服务器中，它的作用是，告诉搜索引擎爬虫，本网站哪些目录下的网页 不希望 你进行爬取收录。
# 在Scrapy启动后，会在第一时间访问网站的 robots.txt 文件，然后决定该网站的爬取范围。
# 当然，我们并不是在做搜索引擎，而且在某些情况下我们想要获取的内容恰恰是被 robots.txt 所禁止访问的。
# 所以，某些时候，我们就要将此配置项设置为 False ，拒绝遵守 Robot协议 ！
ROBOTSTXT_OBEY = False



# 每个pipeline后面有一个数值，这个数组的范围是0-1000，
# 这个数值确定了他们的运行顺序，数字越小越优先
ITEM_PIPELINES = {
   'maomaogougou.pipelines.MaomaogougouPipeline': 300,
}
# 有效的图片存储路径
IMAGES_STORE = 'E:\PythonProject\\'
# 图片失效期限 30天
IMAGES_EXPIRES = 30
