from fastapi import HTTPException
from sqlalchemy.orm import Session
from .model import Book, Article
from .schemas import BookSchema, ArticleSchema
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float
from .config import Base


# Get all book data
def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


Table_names = ["advice_how_to_and_miscellaneous", "audio_fiction", "audio_nonfiction", "business_books",
               "childrens_middle_grade_hardcover",
               "combined_print_and_ebook_fiction", "combined_print_and_ebook_nonfiction", "graphic_books_and_manga",
               "hardcover_fiction", "hardcover_nonfiction",
               "mass_market_monthly", "middle_grade_paperback_monthly", "paperback_nonfiction", "picture_books",
               "series_books", "trade_fiction_paperback",
               "young_adult_hardcover", "young_adult_paperback_monthly"]


# Get books in a category
def get_books_in_category(db: Session, table_name: str):
    if table_name in Table_names:
        class Book(Base):

            __tablename__ = table_name
            __table_args__ = {'extend_existing': True}  # This is to make sure the table is not re-created from scratch
            Id = Column(Integer, primary_key=True, nullable=False)
            rank = Column(Integer)
            rank_last_week = Column(Integer)
            weeks_on_list = Column(Integer)
            publisher = Column(String)
            description = Column(String)
            price = Column(Float)
            title = Column(String)
            author = Column(String)
            contributor = Column(String)
            contributor_note = Column(String)
            book_image = Column(String)
            book_image_width = Column(Integer)
            book_image_height = Column(Integer)
            amazon_product_url = Column(String)
            isbns = Column(String)
            buy_links = Column(String)

        return db.query(Book).filter(Book.__tablename__ == table_name).all()

    else:
        raise HTTPException(status_code=400, detail="Category doesn't exist in database")


def get_book_by_table(db: Session, table_name: str, book_title: str):
    if table_name in Table_names:
        class Book(Base):

            __tablename__ = table_name
            __table_args__ = {'extend_existing': True}  # This is to make sure the table is not re-created from scratch
            Id = Column(Integer, primary_key=True, nullable=False)
            rank = Column(Integer)
            rank_last_week = Column(Integer)
            weeks_on_list = Column(Integer)
            publisher = Column(String)
            description = Column(String)
            price = Column(Float)
            title = Column(String)
            author = Column(String)
            contributor = Column(String)
            contributor_note = Column(String)
            book_image = Column(String)
            book_image_width = Column(Integer)
            book_image_height = Column(Integer)
            amazon_product_url = Column(String)
            isbns = Column(String)
            buy_links = Column(String)

        return db.query(Book).filter(Book.title == book_title).all()

    else:
        raise HTTPException(status_code=400, detail="Table doesn't exist in database")


# def get_book_by_contributor(db:Session, contributor: str, table_name :str): 

#     if table_name in Table_names:
#             class Book(Base):

#                 __tablename__ = table_name
#                 __table_args__ = {'extend_existing': True} #This is to make sure the table is not re-created from scratch
#                 Id= Column(Integer, primary_key=True, nullable=False)
#                 rank= Column(Integer)
#                 rank_last_week= Column(Integer)
#                 weeks_on_list= Column(Integer)
#                 publisher= Column(String)
#                 description= Column(String)
#                 price= Column(Float)
#                 title= Column(String)
#                 author= Column(String)
#                 contributor= Column(String)
#                 contributor_note= Column(String)
#                 book_image= Column(String)
#                 book_image_width= Column(Integer)
#                 book_image_height= Column(Integer)
#                 amazon_product_url= Column(String)
#                 isbns= Column(String)
#                 buy_links= Column(String)

#             return db.query(Book).filter(Book.contributor == contributor).all()
#     else:
#         raise HTTPException(status_code=400, detail="Table doesn't exist in database")


# Get book by title
def get_book_by_name(db: Session, book_title: str):
    return db.query(Book).filter(Book.title == book_title).first()


# Create a new book
def create_book(table_name: str, db: Session, book: BookSchema):
    if table_name in Table_names:
        class Book(Base):
            __tablename__ = table_name
            __table_args__ = {'extend_existing': True}  # This is to make sure the table is not re-created from scratch
            Id = Column(Integer, primary_key=True, nullable=False)
            rank = Column(Integer)
            rank_last_week = Column(Integer)
            weeks_on_list = Column(Integer)
            publisher = Column(String)
            description = Column(String)
            price = Column(Float)
            title = Column(String)
            author = Column(String)
            contributor = Column(String)
            contributor_note = Column(String)
            book_image = Column(String)
            book_image_width = Column(Integer)
            book_image_height = Column(Integer)
            amazon_product_url = Column(String)
            isbns = Column(String)
            buy_links = Column(String)

    _book = Book(Id=book.id, rank=book.rank, rank_last_week=book.rank_last_week, weeks_on_list=book.weeks_on_list,
                 publisher=book.publisher, description=book.description, price=book.price, title=book.title,
                 author=book.author, contributor=book.contributor, contributor_note=book.contributor_note,
                 book_image=book.book_image, book_image_width=book.book_image_width,
                 book_image_height=book.book_image_height,
                 amazon_product_url=book.amazon_product_url, buy_links=book.buy_links)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return book


# update book
# def update_book(table_name: str, db:Session,title: str, description: str, author:str):
#     if table_name in Table_names:
#             class Book(Base):

#                 __tablename__ = table_name
#                 __table_args__ = {'extend_existing': True} #This is to make sure the table is not re-created from scratch
#                 Id= Column(Integer, primary_key=True, nullable=False)
#                 rank= Column(Integer)
#                 rank_last_week= Column(Integer)
#                 weeks_on_list= Column(Integer)
#                 publisher= Column(String)
#                 description= Column(String)
#                 price= Column(Float)
#                 title= Column(String)
#                 author= Column(String)
#                 contributor= Column(String)
#                 contributor_note= Column(String)
#                 book_image= Column(String)
#                 book_image_width= Column(Integer)
#                 book_image_height= Column(Integer)
#                 amazon_product_url= Column(String)
#                 isbns= Column(String)
#                 buy_links= Column(String)
#     _book = get_book_by_name(db=db, title=title)
#     _book.description = description
#     db.commit()
#     db.refresh(_book)
#     return _book


# Get article by section name
def get_article_by_section_name(db: Session, section_name: str):
    return db.query(Article).filter(Article.section_name == section_name).all()


def c_article(db: Session, article: ArticleSchema):
    _article = Article(id=article.id, abstract=article.abstract, web_url=article.web_url,
                       lead_paragraph=article.lead_paragraph,
                       pub_date=article.pub_date, news_desk=article.news_desk, section_name=article.section_name,
                       type_of_material=article.type_of_material,
                       word_count=article.word_count)
    # _article.__tablename__ = table_name
    db.add(_article)
    db.commit()
    db.refresh(_article)
    return _article


# update article
def update_article(db: Session, id: str):
    _article = get_article_by_section_name(db=db, id=id)

    db.commit()
    db.refresh(_article)
    return _article
