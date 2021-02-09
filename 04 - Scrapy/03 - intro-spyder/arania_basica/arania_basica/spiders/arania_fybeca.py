import scrapy
class IntroSpyder(scrapy.Spider):
    name="fybeca"
    ursl=['https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25']
    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    def parse(self,response):
        etiqueta_contenedora=response.css('.product-tile-inner')
        titulo=etiqueta_contenedora.css('.name::text').extract()
        imagen_url=etiqueta_contenedora.css('#gImg::attr(src)').extract()
        price_member=etiqueta_contenedora.css('.price-member > div:nth-child(1)::attr(data-bind)').extract()
        price=etiqueta_contenedora.css('.price::attr(data-bind)').extract()
        price_member_value=[]
        price_value=[]
        ahorro=[]
        for p in price_member:
            
            price_member_value.append(float(p.split('(', 1)[1].split(')')[0]))
        for p in price:
            price_value.append(float(p.split('(', 1)[1].split(')')[0]))
            ahorro=price_value-price_member_value
        print(ahorro)