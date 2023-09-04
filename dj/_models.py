from __future__ import annotations

from typing import Optional, Any, Union

from pydantic import BaseModel, Field, condecimal, HttpUrl


class Description(BaseModel):
    html: list[str]
    text: str

class Manufacturer(BaseModel):
    name: str
    website: Website

class Website(BaseModel):
    name: str
    link: HttpUrl

class AdditionalImage(BaseModel):
    name: str
    link: Optional[HttpUrl]

class Data(BaseModel):
    link: HttpUrl
    sku: str
    name: Optional[str] = None
    main_image: Optional[HttpUrl] = None
    products_id: Optional[Any] = 0
    title: Optional[str] = None
    keywords: Optional[str] = None
    short_desc: Optional[str] = None
    price: Optional[Any] = 0
    manufacturer: Optional[str] = None
    description: Optional[str] = None
    
    image_urls:  Optional[list[str]] = None
    breadcrumbs:  Optional[list[str]] = None
    discount_tiers:  Optional[list[str]] = None
    discount_amount:  Optional[list[str]] = None