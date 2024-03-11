from fastapi import APIRouter, HTTPException, Path, Depends, status
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from .schemas import BookSchema, RequestBook, ReponseBook, RequestArticle, ReponseArticle, ArticleSchema
from . import crud
from .config import SessionLocal
from sqlalchemy import func
from fastapi import Path
from typing import Optional, List
from . import schemas, model
from .model import Article

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Table_names = ["advice_how_to_and_miscellaneous", "audio_fiction", "audio_nonfiction", "business_books",
               "childrens_middle_grade_hardcover",
               "combined_print_and_ebook_fiction", "combined_print_and_ebook_nonfiction", "graphic_books_and_manga",
               "hardcover_fiction", "hardcover_nonfiction",
               "mass_market_monthly", "middle_grade_paperback_monthly", "paperback_nonfiction", "picture_books",
               "series_books", "trade_fiction_paperback",
               "young_adult_hardcover", "young_adult_paperback_monthly"]

section_names = ['Business Day', 'Technology', 'Podcasts', 'Science', 'World',
                 'Style', 'Travel', 'New York', 'Health', 'Opinion', 'T Brand',
                 'Arts', 'U.S.', 'Magazine', 'Books', 'Movies', 'The Upshot',
                 'Fashion & Style', 'Climate', 'Food', 'Times Insider', 'Well',
                 'Theater', 'Automobiles', 'Job Market', 'Reader Center', 'Sports',
                 'T Magazine', 'Blogs', 'Home & Garden', 'Education',
                 'The Learning Network', 'Real Estate', 'Briefing', 'Obituaries',
                 'At Home', 'Crosswords & Games', 'Week in Review', 'Archives',
                 'readersopinions', 'Your Money', 'Neediest Cases',
                 'Sunday Review']


# WORKS WELL


# @router.get("/book/{title}", description= "This path is used to get a book using the title from the category. \
#             \nAvailable categories: \
#             \n- advice_how_to_and_miscellaneous \
#             \n- audio_fiction \
#             \n- audio_nonfiction \
#             \n- business_books \
#             \n- childrens_middle_grade_hardcover \
#             \n- combined_print_and_ebook_fiction \
#             \n- combined_print_and_ebook_nonfiction \
#             \n- graphic_books_and_manga \
#             \n- hardcover_fiction \
#             \n- hardcover_nonfiction \
#             \n- mass_market_monthly \
#             \n- middle_grade_paperback_monthly \
#             \n- paperback_nonfiction \
#             \n- picture_books \
#             \n- series_books \
#             \n- trade_fiction_paperback \
#             \n- young_adult_hardcover \
#             \n- young_adult_paperback_monthly")

# async def get_by_title_and_category(table_name :str, title:str=Path(..., description="The title should be written in CAPITAL LETTERS."), db: Session = Depends(get_db)):
#     if table_name in Table_names:
#         _book = crud.get_book_by_table(db,table_name,title)
#         print(_book)
#         return ReponseBook(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)
#     else:
#         raise HTTPException(status_code=400, detail="Table doesn't exist in database") 


@router.get("/book/{category}", description="This path is used to get books in a category. \
            \nAvailable categories: \
            \n- advice_how_to_and_miscellaneous \
            \n- audio_fiction \
            \n- audio_nonfiction \
            \n- business_books \
            \n- childrens_middle_grade_hardcover \
            \n- combined_print_and_ebook_fiction \
            \n- combined_print_and_ebook_nonfiction \
            \n- graphic_books_and_manga \
            \n- hardcover_fiction \
            \n- hardcover_nonfiction \
            \n- mass_market_monthly \
            \n- middle_grade_paperback_monthly \
            \n- paperback_nonfiction \
            \n- picture_books \
            \n- series_books \
            \n- trade_fiction_paperback \
            \n- young_adult_hardcover \
            \n- young_adult_paperback_monthly")
def get_books_in_category(Category: str, db: Session = Depends(get_db)):
    if Category in Table_names:
        _book = crud.get_books_in_category(db, Category)
        print(_book)
        return ReponseBook(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=400, detail="Category doesn't exist in database")

    # @router.get("/book/{title}", description= "This path is used to get a book using the title from the category. \


#             \nAvailable categories: \
#             \n- advice_how_to_and_miscellaneous \
#             \n- audio_fiction \
#             \n- audio_nonfiction \
#             \n- business_books \
#             \n- childrens_middle_grade_hardcover \
#             \n- combined_print_and_ebook_fiction \
#             \n- combined_print_and_ebook_nonfiction \
#             \n- graphic_books_and_manga \
#             \n- hardcover_fiction \
#             \n- hardcover_nonfiction \
#             \n- mass_market_monthly \
#             \n- middle_grade_paperback_monthly \
#             \n- paperback_nonfiction \
#             \n- picture_books \
#             \n- series_books \
#             \n- trade_fiction_paperback \
#             \n- young_adult_hardcover \
#             \n- young_adult_paperback_monthly")

# def get_by_title_and_category(table_name :str, title:str=Path(..., description="The title should be written in CAPITAL LETTERS."), db: Session = Depends(get_db)):
#     if table_name in Table_names:
#         _book = crud.get_book_by_table(db,table_name,title)
#         print(_book)
#         return ReponseBook(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)
#     else:
#         raise HTTPException(status_code=400, detail="Table doesn't exist in database") 


# @router.get("/book/{contributor}", description= "This path is used to get a book using the author from the category")
# async def get_by_contributor(table_name :str, contributor:str=Path(..., description="The initials should be in capital letters."), db: Session = Depends(get_db)):
#     if table_name in Table_names:
#         _book = crud.get_book_by_author(db,contributor, table_name)
#         return _book
#     else:
#         raise HTTPException(status_code=400, detail="Table doesn't exist in database") 


# #Get book by author
# @router.get("/book/{author}", description= "This path is used to get book by author for a paticular category")
# async def get(table_name:str, author: str, db:Session=Depends(get_db)):
#     if table_name in Table_names:

#         _book = crud.get_book_by_author(db,author,table_name)
#         print(_book)
#         return ReponseBook(code=200, status="Ok", message="Success fetch all data", result=_book).dict(exclude_none=True)
#     else:
#         raise HTTPException(status_code=400, detail="Table doesn't exist in database") 

@router.get("/article/{section_name}", description="This path is used to get an article using the section name. This process could take some time because there alot of articles. \
            \nAvailable section names: \
            \n- Crosswords & Games \
            \n- U.S. \
            \n- Theater \
            \n- Times Insider \
            \n- Education \
            \n- Obituaries \
            \n- Business Day \
            \n- Sports \
            \n- T Magazine \
            \n- Real Estate \
            \n- Home & Garden \
            \n- New York \
            \n- Reader Center \
            \n- Job Market \
            \n- The Learning Network \
            \n- Sunday Review \
            \n- Arts \
            \n- Week in Review \
            \n- Magazine \
            \n- Fashion & Style \
            \n- At Home \
            \n- Technology \
            \n- Podcasts \
            \n- Science \
            \n- World \
            \n- Style \
            \n- Travel \
            \n- Health \
            \n- Opinion \
            \n- T Brand \
            \n- Books \
            \n- Movies \
            \n- The Upshot \
            \n- Climate \
            \n- Food \
            \n- Well \
            \n- Automobiles \
            \n- Blogs \
            \n- Briefing \
            \n- Archives \
            \n- readersopinions\
            \n- Your Money \
            \n- Neediest Cases")
async def get_by_section_name(section_name: str = Path(..., description="The initials should be in capital letters."),
                              db: Session = Depends(get_db)):
    if section_name in section_names:

        article = crud.get_article_by_section_name(db, section_name)

        # print(article)
        return ReponseArticle(code=200, status="Ok", message="Success get data", result=article).dict(exclude_none=True)
    else:
        raise HTTPException(status_code=400, detail="Section name doesn't exist")


@router.put('/create/{book}')
async def create_book(table_name: str, request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(table_name, db, book=request.parameter)
    return ReponseBook(code=200, status="Ok", message="Book created successfully").dict(exclude_none=True)


# @router.put("/update/{book}")
# async def update_book(table_name: str, request: RequestBook, db:Session = Depends(get_db)):
#     _book = crud.update_book(table_name, db,title=request.parameter.title, description=request.parameter.description,
#     author=request.parameter.author)
#     return ReponseBook(code=200, status="Ok", message="Success update data", result=_book).dict(exclude_none=True)


@router.post("/create/{article}")
def create_article(request: RequestArticle, db: Session = Depends(get_db)):
    crud.c_article(db, article=request.parameter)
    return ReponseArticle(code=200, status="Ok", message="Article created successfully").dict(exclude_none=True)

# @router.post("/update/{article}")
# async def update_article(request: RequestArticle, db:Session = Depends(get_db)):
#     print("test")
#     _article= crud.update_article(db,id=request.parameter.id)
#     return ReponseArticle(code=200, status="Ok", message="Success update data", result=_article).dict(exclude_none=True)
