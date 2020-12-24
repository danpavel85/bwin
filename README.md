# USE SCRAPY AND TOR

To install Tor, Vidalia and Polipo for Windows go to https://stackoverflow.com/questions/32054558/scrapy-with-tor-windows and follow the instructions

1.-- in scrapy settings.py file:

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'

HTTP_PROXY = 'http://127.0.0.1:8123'

DOWNLOADER_MIDDLEWARES = {
    'tor_spider.middlewares.ProxyMiddleware': 410,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

2.-- in middlewares.py file:

from scrapy.conf import settings

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

3.-- go to firefox browser -- options/network settings/manual proxy configuration/ HTTP Proxy: localhost/ Port: 8123
									                                                              / HTTPS Proxy: localhost/ Port: 8123
4.-- start vidalia

5.-- start polipo
in to the folder where you unzipped the polipo files open cmd and enter the next command:
polipo.exe -c config.sample
