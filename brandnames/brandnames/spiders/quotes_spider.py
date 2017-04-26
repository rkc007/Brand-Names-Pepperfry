import scrapy
class QuotesSpider(scrapy.Spider):
	name = "quotes"

	start_urls = [
		'https://www.pepperfry.com/brands.html',
	]
	def parse(self, response):
		for shit in response.xpath('//ul[@class="gb-scroll"]/li/a/@href').extract():
			self.logger.info((shit))
			#self.logger.info(response.urljoin(shit))
			yield scrapy.Request(response.urljoin(shit),callback=self.get_brands)
			
			
	def get_brands(self, response):
		shit_weed=[]
		for fuckthislife in response.xpath('//ul[@class="brand-division-list clearfix"]/li/a'):
			shit_weed.append({'name':fuckthislife.xpath('//text()').extract(), 'shop_link':'got fucked'})
		self.logger.info(shit_weed)
		#yield {
		#	'category' : response.xpath('//*[@id="brandCategoryTabActive"]/li/a/label/text()').extract()[0],
		#	'brands' : [{'name':ass,'shop_link':back} for ass,back in response.xpath('//ul[@class="brand-division-list clearfix"]/li/a/text()').extract()]
		#}
		#self.logger.info(response.xpath('//*[@id="brandCategoryTabActive"]/li/a/label/text()').extract())
		#self.logger.info(response.body)
		#for ass in response.xpath('//ul[@class="brand-division-list clearfix"]/li/a/text()').extract():
		#	self.logger.info(ass)
		