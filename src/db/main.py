from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
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
        statement = text("SELECT 'hello';")
        
        result = await conn.execute(statement)
        
        print(result.all())