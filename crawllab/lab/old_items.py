# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Field

from pydantic import BaseModel

class MyItem(scrapy.Item):
    id = scrapy.Field()
    
class CKKItem(scrapy.Item):
    
    link: str = Field(serializer=str)
    sku: str = Field(serializer=str)
    name: str = Field(serializer=str)
    main_image: str = Field(serializer=str)
    products_id: str = Field(serializer=str)
    title: str = Field(serializer=str)
    keywords: str = Field(serializer=str)
    short_desc: str = Field(serializer=str)
    price: str = Field(serializer=str)
    description: str = Field(serializer=str)
    manufacturer: str = Field(serializer=str)
    
    image_urls: Field(serializer=list)
    breadcrumbs:  Field(serializer=list)
    discount_tiers: Field(serializer=list)
    discount_amount: Field(serializer=list)


   
class DataField(BaseModel):
    id: int
    fields: dict[str, str]
    list_fields: list[str]
    
class DataItem(BaseModel):  
    link: str = Field(serializer=str)
    sku: str = Field(serializer=str)
    name: str = Field(serializer=str)
    main_image: str = Field(serializer=str)
    products_id: str = Field(serializer=str)
    title: str = Field(serializer=str)
    keywords: str = Field(serializer=str)
    short_desc: str = Field(serializer=str)
    price: str = Field(serializer=str)
    description  : str = Field(serializer=str)
    manufacturer  : str = Field(serializer=str)
    
    image_urls: list[str] = []
    breadcrumbs:  list[str] = []
    discount_tiers: list[str] = [] 
    discount_amount: list[str] = []

