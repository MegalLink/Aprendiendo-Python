import scrapy

from scrapy.item import Field,Item
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose

class PeliculaItem(Item):
    generos=Field()
    titulo=Field()
    temporadas=Field()
    actores=Field()
    #descripcion=Field()
    puntaje=Field()
    estado=Field()
    fecha_estreno=Field()
    

class SeriesFlixSpider(CrawlSpider):
    custom_settings={
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
        #'CLOSESPIDER_PAGECOUNT':2000       
    }
    name = 'seriesflix'
    
    allowed_domains = ['seriesflix.to',]
    start_urls = ['https://seriesflix.to/']
    #download_delay=1
    
    rules={
        Rule(# Paginacion de letras
        LinkExtractor(allow=r"/letras/"),follow=True
        ),
        Rule( #Detalle series
        LinkExtractor(
            allow=r'/series/'
            
        ),follow=True,callback='parse_items'
    ),
    }
    def limpiar_texto(self,texto):
        
        nuevo_texto=texto.replace('\"','').strip()
        print("LIMPIAR",nuevo_texto)
        return nuevo_texto
    def parse_items(self, response):       
        item=ItemLoader(PeliculaItem(),response)
        item.add_css('titulo','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > h1::text',output_proccesor = [TakeFirst(),MapCompose(self.limpiar_texto)])
        item.add_css('generos','.TPMvCn>.Description>.Genre>a::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        item.add_css('temporadas','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > p > span:nth-child(1)::text',output_proccesor = [TakeFirst(),MapCompose(self.limpiar_texto)])
        item.add_css('actores','.TPMvCn>.Description>.Cast> a::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        #item.add_css('descripcion','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > div.Description > p:nth-child(1)::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        item.add_css('puntaje','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > div.Info > div > div > span::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        item.add_css('estado','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > div.Info > span.Qlty::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        item.add_css('fecha_estreno','#Tf-Wp > div.Tf-Wp > div > div.MovieListSldCn > article > header > div.TPMvCn > div.Info > span.Date::text',output_proccesor= [MapCompose(self.limpiar_texto)])
        yield item.load_item()