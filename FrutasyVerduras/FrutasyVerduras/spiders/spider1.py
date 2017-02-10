# -*- coding: utf-8 -*-
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from FrutasyVerduras.items import *


# Página  : http://www.lavegadelivery.cl/

class Lavegadelivery(Spider):
    name="lavegadelivery"
    start_urls = ["http://www.lavegadelivery.cl/categoria.php?cat=1",
                  "http://www.lavegadelivery.cl/categoria.php?cat=2"]

    allow_domains= ['lavegadelivery.cl']

    #Entra a las 2 url, conveniente ya que los codigos son los mismos.
    #Filtrar unidades de medida
    def parse(self, response):
        sel = Selector(response)
        item  = Atributos()
        for sel in sel.xpath('//section[@id="cuerpo"]/div[@class="cuadro"]'):
            item['Producto'] = sel.xpath('.//p[@class="nombre"]/text()').extract()
            item['Precio']= sel.xpath('.//p[@class="precio"]/text()').extract()
            item['Fuente']= 'www.lavegadelivery.cl'
            #Datos convertidos a string
            p = (item['Producto'][0]).encode('utf-8')
            datos_precio = (item['Precio'][0]).encode('utf-8').strip("$").split('-')
            row = {'Producto': p, 'Precio': datos_precio[0],'Fuente': item['Fuente'], 'Observaciones':datos_precio[1]}
            #aux.append(row)
            yield row
