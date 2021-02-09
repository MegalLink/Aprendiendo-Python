# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem # DropItem

class ProyectoscrapyPipeline:
    def process_item(self, item, spider):
        return item
class ExisteTitulo(object):
    def process_item(self, item, spider):
        titulo = item['titulo']
        if(len(titulo) is 0):
            raise DropItem('No tiene capsula')
        else:
            return item