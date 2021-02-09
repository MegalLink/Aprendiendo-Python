import scrapy
class IntroSpyder(scrapy.Spider):
    name="introduccion_spyder"
    ursl=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']
    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    def parse(self,response):
        etiqueta_contenedora=response.css('article.product_pod')
        titulos=etiqueta_contenedora.css('h3>a::text').extract()
        image_url=etiqueta_contenedora.css('.thumbnail::attr(src)').extract()
        precio=etiqueta_contenedora.css('.price_color::text').extract()
        in_stock=etiqueta_contenedora.css('.availability::text').extract()
        estrellas= response.css('.star-rating').xpath("@class").extract()
        puntos_estrellas=['zero','one','two','three','four','five']
        for estrella in estrellas:
            filtrado=estrella.replace('star-rating','').lower().strip() 
            print(f'{filtrado} -> {puntos_estrellas.index(filtrado)}')
           