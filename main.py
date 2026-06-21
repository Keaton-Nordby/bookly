from fastapi import FastAPI, status, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt & David Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-30",
        "page_count": 352,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Design Patterns",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-21",
        "page_count": 395,
        "language": "en",
    },
    {
        "id": 4,
        "title": "Refactoring",
        "author": "Martin Fowler",
        "publisher": "Addison-Wesley",
        "published_date": "1999-07-08",
        "page_count": 448,
        "language": "English",
    },
    {
        "id": 5,
        "title": "You Don't Know JS Yet",
        "author": "Kyle Simpson",
        "publisher": "Independently Published",
        "published_date": "2020-01-28",
        "page_count": 278,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2015-08-20",
        "page_count": 792,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book


@app.get("/book/{book_id}")
async def update_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


app.get("/book/{book_id}")
async def delete_book(book_id: int):
    pass
