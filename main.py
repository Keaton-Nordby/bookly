from fastapi import FastAPI

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "publisher": "Addison-Wesley",
        "published_date": "1999-10-30",
        "page_count": 352,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publisher": "MIT Press",
        "published_date": "2009-07-31",
        "page_count": 1312,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Design Patterns",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "publisher": "Addison-Wesley",
        "published_date": "1994-10-21",
        "page_count": 395,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Refactoring",
        "author": "Martin Fowler",
        "publisher": "Addison-Wesley",
        "published_date": "1999-07-08",
        "page_count": 431,
        "language": "English"
    },
    {
        "id": 6,
        "title": "You Don't Know JS Yet",
        "author": "Kyle Simpson",
        "publisher": "Independently Published",
        "published_date": "2020-01-28",
        "page_count": 143,
        "language": "English"
    }
]


@app.get('/books')
async def get_all_books():
    return books


@app.post('/books')
async def create_a_book() -> dict:
    pass


@app.get('/books/{book_id}')
async def get_book(book_id: int) -> dict:
    pass


@app.put('/book/{book_id}')
async def get_all_books(book_id: int) -> dict:
    pass


@app.delete('/books/{book_id}')
async def delete_a_book(book_id: int) -> dict:
    pass

