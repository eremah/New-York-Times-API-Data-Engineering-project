
from pydantic import BaseModel
from .config import Base
from sqlalchemy.sql.expression import null
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship




Table_names = ["advice_how_to_and_miscellaneous", "audio_fiction", "audio_nonfiction", "business_books", "childrens_middle_grade_hardcover",
               "combined_print_and_ebook_fiction","combined_print_and_ebook_nonfiction", "graphic_books_and_manga", "hardcover_fiction", "hardcover_nonfiction", 
               "mass_market_monthly", "middle_grade_paperback_monthly", "paperback_nonfiction", "picture_books", "series_books", "trade_fiction_paperback",
               "young_adult_hardcover", "young_adult_paperback_monthly"]


class Book(Base):

    
    __tablename__ = "advice_how_to_and_miscellaneous" #Default table 
    Id= Column(Integer, primary_key=True, nullable=False)
    rank= Column(Integer)
    rank_last_week= Column(Integer)
    weeks_on_list= Column(Integer)
    publisher= Column(String)
    description= Column(String)
    price= Column(Float)
    title= Column(String)
    author= Column(String)
    contributor= Column(String)
    contributor_note= Column(String)
    book_image= Column(String)
    book_image_width= Column(Integer)
    book_image_height= Column(Integer)
    amazon_product_url= Column(String)
    isbns= Column(String)
    buy_links= Column(String)


class Article(Base):

    
    __tablename__ = "NYT_Articles" #Default table 
    id= Column(Integer, primary_key=True, nullable=False)
    abstract= Column(String)
    web_url= Column(String)
    lead_paragraph= Column(String)
    pub_date= Column(String)
    news_desk= Column(String)
    section_name= Column(String)
    type_of_material= Column(String)
    word_count= Column(Integer)
    


