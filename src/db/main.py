from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.books.models import Book
from src.config import Config




# database connection engine
engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True
))


# function to keep db running while app is being used
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        
        