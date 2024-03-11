from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

# class ArticleSchema(BaseModel):
#     id: int
#     uri: str
#     news_desk: str
#     section_name: str
#     word_count: int

#     class Config:
#         orm_mode = True


# class RequestArticle(BaseModel):
#     parameter: ArticleSchema = Field(...)


# class ReponseArticle(GenericModel,Generic[T]):
#     code: str
#     status: str
#     message: str
#     result : Optional[T]





class BookSchema(BaseModel):

    id: int
    rank: int
    rank_last_week: int
    weeks_on_list: int
    publisher: str
    description: str
    price: float
    title: str
    author: str
    contributor: str
    contributor_note: str
    book_image: str
    book_image_width: int
    book_image_height: int
    amazon_product_url: str
    isbns: str
    buy_links: str


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)


class ReponseBook(GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result : Optional[T]


class ArticleSchema(BaseModel):

    id: int
    abstract: str
    web_url: str
    lead_paragraph: str
    pub_date: str
    news_desk: str
    section_name: str
    type_of_material: str
    word_count: int


class RequestArticle(BaseModel):
    parameter: ArticleSchema = Field(...)


class ReponseArticle(GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result : Optional[T]