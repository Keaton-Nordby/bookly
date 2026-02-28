from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
import uuid

from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from src.books.service import BookService
from src.db.main import get_session


book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    return await book_service.get_all_books(session)


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel,
    session: AsyncSession = Depends(get_session),
):
    return await book_service.create_book(book_data, session)


@book_router.get("/{book_uid}", response_model=Book)
async def get_book(
    book_uid: uuid.UUID,
    session: AsyncSession = Depends(get_session),
):
    book = await book_service.get_book(book_uid, session)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: uuid.UUID,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
):

    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(
    book_uid: uuid.UUID,
    session: AsyncSession = Depends(get_session),
):

    deleted_book = await book_service.delete_book(book_uid, session)

    if not deleted_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return None
