import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class CrawlOnuSpider(CrawlSpider):
    name = 'crawl_onu'
    allowed_domains = ['un.org']
    start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html']

    regla_uno={
        Rule(
            LinkExtractor(),
            callback='parse_page' #nombre de la funcion a ejecutar para parsear
        ),#segundo parametro vacio debe ir esa coma
    }
   
    segmentos_url_permitidos=('funds-programmes-specialized-agencies-and-others/')
    regla_dos={Rule(
        LinkExtractor(
            allow_domains=allowed_domains,allow=segmentos_url_permitidos
        ),callback='parse_page'
    ),
    }
    segmentos_restringidos=('ar/sections','zh/sections','ru/sections')
    regla_tres={Rule(
        LinkExtractor(
            allow_domains=allowed_domains,allow=segmentos_url_permitidos,deny=segmentos_restringidos
        ),callback='parse_page'
    ),
    }
    rules=regla_tres
    def parse_page(self,response):
        lista_programas=response.css('.content>.field>div.field-items>div.field-item>h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencias.txt','a+',encoding='utf-8') as archivo:
                archivo.write(agencia+'\n')