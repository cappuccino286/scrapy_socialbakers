# -*- coding: utf-8 -*-
import scrapy

class TopbrandSpider(scrapy.Spider):
    name = 'topbrand'
    start_urls = ['/']

    def __init__(self, country='france', *args, **kwargs):
        super(TopbrandSpider, self).__init__(*args, **kwargs)
        brand = getattr(self, 'brand', '')
        if brand:
            brand= '/'+brand
        self.start_urls = ['http://www.socialbakers.com/statistics/facebook/pages/total/%s/brands%s/page-1-5/' %(country,brand)]

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
    	tagLinks=response.css('.account-detail .account-tag-list li a')
    	tags=[]
    	for link in enumerate(tagLinks):
    		if link[1].xpath('i/@data-icons-before').re("\ue642"):
    			tagTexts = link[1].xpath('text()').extract()
    			for tagText in tagTexts:
    				tagTextAfterStrip = tagText.strip()
    				if tagTextAfterStrip:
    					tags.append(tagTextAfterStrip)
    	yield{
    		'pos':pos,
    		'brand_name':brand_name,
    		'url_page':response.css('.account-detail .account-list a.link-nw::attr(href)').extract_first(),
    		'fans':"".join(fans.split()),
			'tags':tags,
    		'image_urls':img_url
    	}
