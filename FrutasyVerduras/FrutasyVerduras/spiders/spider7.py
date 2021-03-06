#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader
from FrutasyVerduras.items import *

#Página : https://www.fullmercado.cl/

class FullMercado(Spider):
    name="Vega virtual "
    start_urls = ["https://www.fullmercado.cl/tienda/"]
    allow_domains = ['fullmercado.cl']
    
    def parse(self, response):
        sel = Selector(response)
        item = Atributos()
        verduras = sel.xpath('//div[@class="et_pb_module et_pb_shop  et_pb_shop_1"]/div/ul/li')
        for sel in verduras:
            item['Producto'] = sel.xpath('a/h3/text()').extract()
            item['Precio'] = sel.xpath('a/span[2]/span/text()').extract()
            
            print item #print (item['Precio'][0]).encode('utf-8')

        #formato \xa0
        frutas = sel.xpath('//div[@class="et_pb_module et_pb_shop  et_pb_shop_2"]/div/ul/li') 
        for sel in frutas:
            item['Producto'] = sel.xpath('a/h3/text()').extract()
            item['Precio'] = sel.xpath('a/span[2]/span/text()').extract()
            print item#(item['Producto'][0]).encode('utf-8')

