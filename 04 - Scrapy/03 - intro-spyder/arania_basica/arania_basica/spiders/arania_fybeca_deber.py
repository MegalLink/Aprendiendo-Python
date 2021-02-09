import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import pandas as pd

class FybecaCrawl(CrawlSpider):
    name = 'arania_fybeca_deber' # heredado

    allowed_domains = [ # heredado
        'fybeca.com'
    ]

    numero = '5000'
    
    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&pp={}&s=-1'.format(numero),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&pp={}&s=-1'.format(numero),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&pp={}&s=-1'.format(numero),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&pp={}&s=-1'.format(numero),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&pp={}&s=-1'.format(numero),
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&pp={}&s=-1'.format(numero),
    ]

    segmentos_url_permitidos = ( 
        'cat=446&pp={}&s=-1'.format(numero),
        'cat=537&pp={}&s=-1'.format(numero),
        'cat=627&pp={}&s=-1'.format(numero),
        'cat=558&pp={}&s=-1'.format(numero),
        'cat=489&pp={}&s=-1'.format(numero),
        'cat=562&pp={}&s=-1'.format(numero),
    )

    segmentos_url_restringidos = (
        'pages/detail.jsf'
    )

    regla = (
        Rule(
            LinkExtractor(
                allow_domains= allowed_domains,
                allow= segmentos_url_permitidos,
                deny=segmentos_url_restringidos,
            ),
            callback= 'parse_page'
        ),
        # parametro vacio
    )

    rules = regla


    def parse_page(self,response):

        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )

        url_imagen = list(etiqueta_contenedora.css(
            "div.detail > a.image > img#gImg.productImage::attr(src)"
        ).extract())
        precio_general = etiqueta_contenedora.css(
            "div.detail > div.side > div.price::attr(data-bind)"
        ).extract()  
        productos = list(etiqueta_contenedora.css(
            "a.name::text"
        ).extract())
              
        precio_afiliado = list(etiqueta_contenedora.css(
            "div.detail > div.side > div.price-member > div::attr(data-bind)"
        ).extract())
    
        precio_afiliado_total = list()
        for i in precio_afiliado:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            precio_afiliado_total.append(precio)

        print("Más cotoso siendo miembro afiliado:"+ str(max(precio_afiliado_total)))
        print("Más economico siendo miembro afiliado:"+ str(min(precio_afiliado_total)))
        print("Total Afiliado: "+str(sum(precio_afiliado_total)))

        precio_general_total = list()
        for i in precio_general:
            precio = float(i.replace("text:'$' + (","").replace(").formatMoney(2, '.', ',')",""))
            precio_general_total.append(precio)      
        print("Más económico:"+ str(min(precio_general_total)))
        print("Más costoso:"+ str(max(precio_general_total)))
        print("Total Original: "+str(sum(precio_general_total)))
        suma_original = sum(precio_general_total)
        suma_afiliado = sum(precio_afiliado_total)
        print('Ahorro calculado siendo afiliado:' + str(suma_original - suma_afiliado)) 
        
        resultado = pd.DataFrame(zip(productos,
                                    url_imagen,
                                    precio_general_total, 
                                    precio_afiliado_total), columns=['Productos','Imagen','Precio original', 'Precio afiliado'])

        
        resultado['Diferencia precios'] = resultado['Precio original'] - resultado['Precio afiliado']        
        lista_resultados = resultado.values.tolist()                
        for result in lista_resultados:
            for i in result: 
                data = str(i)               
                with open('fybeca.txt', 'a+', encoding = 'utf-8') as archivo:
                    archivo.write(data + ',')
            with open('fybeca.txt', 'a+', encoding = 'utf-8') as archivo:
                archivo.write('\n')