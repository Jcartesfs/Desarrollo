#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from FrutasyVerduras.items import *

#Página : http://www.tottus.cl/

class tottus(Spider):
    name="Tottus "
    start_urls = ["http://www.tottus.cl/tottus/browse/Frescos-Verduras-Papa-y-Tomates/_/N-1u09wo2",
                 "http://www.tottus.cl/tottus/browse/Frescos-Frutas-Paltas-y-Plátanos/_/N-6ytsug",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Lechugas-y-Hortalizas/_/N-ki8en",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Zapallos/_/N-167y1fo",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Cebollas-y-Zanahorias/_/N-1488kp0",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Pepino-y-Apios/_/N-1raumw",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Ensaladas-Listas/_/N-l9uose",
                 "http://www.tottus.cl/tottus/browse/Frescos-Verduras-Otras-Verduras/_/N-g2ddw8",
                 "http://www.tottus.cl/tottus/browse/Frescos-Frutas-Limones-Naranjas-y-C%C3%ADtricos/_/N-1102po5",
                 "http://www.tottus.cl/tottus/product/Frescos-y-Lacteos-Frutas-Manzanas-y-Peras/Brand-FRUTAS/_/R-product-06900092..catalog20001.es.salePricesCL__listPricesCL.tottusCl",
                 "http://www.tottus.cl/tottus/product/Frescos-Frutas-Otras-Frutas/Frescos-Frutas-Pi%C3%B1as-y-Fruta-Tropical/Brand-FRUTAS/_/R-product-05014013..catalog20001.es.salePricesCL__listPricesCL.tottusCl",
                 "http://www.tottus.cl/tottus/browse/Frescos-Frutas-Otras-Frutas/_/N-e0rhub"]
    allow_domains=['tottus.cl']

    def parse(self, response):
        sel = Selector(response)
        for sel in sel.xpath('//div[@class=" item-product-caption"]'):
            item = Atributos()
            item['Producto'] = sel.xpath('div[3]/div[1]/a/h5/div/text()').extract()
            #Recordar precio anterior y precio oferta
            item['Precio']= sel.xpath('div[3]/div[4]/span/span[1]/text()').extract()
            #item['Precio'] = sel.xpath('div[3]/div[5]/text()').extract()   #Precio por unidad
            item['Observaciones'] = sel.xpath('div[3]/div[2]/text()').extract()
            item['Fuente'] = "www.tottus.cl"
            #print type(item['Producto'][0])
            #yield item ((item['Producto'][0]).encode('utf-8')).lstrip(" ")
            #Opcional convertir a string y manipular datos
            p = (item['Producto'][0]).encode('utf-8')#.split('-')
            datos_precio = (item['Precio'][0]).encode('utf-8').strip("$")
            row = {'Producto': p, 'Precio': datos_precio,'Fuente': item['Fuente'], 'Observaciones':""}
            print row
    