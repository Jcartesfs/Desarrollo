from scrapy.item import Field
from scrapy.item import Item

#Se designan atributos globales 
class Atributos(Item):
	Producto = Field()
	Precio = Field()
	Observaciones = Field()
	Fuente = Field() 

	def convert(varible):
		print variable
		if variable:
			variable = str(variable[0])
			return variable 
		return ""