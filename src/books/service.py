from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel


#logic for crud operations, that will be passed to routes -> to main
class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass
    
    async def get_book(self, book_uid: str, session: AsyncSession):
        pass
    
    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        pass
    
    async def update_book(self, book_uid: str, update_date: BookUpdateModel, session: AsyncSession):
        pass
    
    async def delete_book(self, book_uid: str, session: AsyncSession):
        pass
    
    
    