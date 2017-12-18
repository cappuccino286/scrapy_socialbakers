# -*- coding: utf-8 -*-
import scrapy

class TopbrandSpider(scrapy.Spider):
    name = 'topbrand'
    start_urls = ['/']

    def __init__(self, country='france', *args, **kwargs):
        super(TopbrandSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.socialbakers.com/statistics/facebook/pages/total/%s/brands/page-1-5/' % country]

    def parse(self, response):
        for brand in response.css("table.brand-table-list tr"):
        	url_follow=brand.css('.name .item a.acc-placeholder-img::attr(href)').extract_first()
        	brand_name=brand.css('.name .item h2 .show-name::text').extract_first().strip()
        	position=brand.css('.item.item-count::text').extract_first().strip()
        	yield response.follow(url_follow, callback=self.parse_brand,meta={'pos':position,'brand_name':brand_name})

    def parse_brand(self,response):
    	pos=response.meta['pos']
    	brand_name=response.meta['brand_name']
        fans=response.css('.account-detail span.p-nw strong::text').extract_first().strip()
    	img_url=response.css('.account-detail div.img img::attr(src)').extract()
    	yield{
    		'pos':pos,
    		'brand_name':brand_name,
    		'url_page':response.css('.account-detail .account-list a.link-nw::attr(href)').extract_first(),
    		'fans':"".join(fans.split()),
    		'image_urls':img_url,
    	}
