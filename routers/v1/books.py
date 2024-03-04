from typing import Annotated

from fastapi.responses import ORJSONResponse
from icecream import ic
from fastapi import Response, status, APIRouter, Depends
from sqlalchemy import select
from schemas import IncomingBook, ReturnedAllBooks, ReturnedBook
from configurations.database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession

from models.books import Book


COUNTER = 0  # каунтер имитирующий присвоение id в базе данных

books_router = APIRouter(
    tags=["books"],
    prefix="/books"
)

DBSession = Annotated[AsyncSession, Depends(get_async_session)]


# Ручка для создания записи о книге в БД. Возвращает созданную книгу.
@books_router.post("/", response_model=ReturnedBook, status_code=status.HTTP_201_CREATED)  # Прописываем модель ответа
async def create_book(
    book: IncomingBook, session: DBSession
):  # прописываем модель валидирующую входные данные и сессию как зависимость.
    # это - бизнес логика. Обрабатываем данные, сохраняем, преобразуем и т.д.
    new_book = Book(
        title=book.title,
        author=book.author,
        year=book.year,
        count_pages=book.count_pages,
    )
    session.add(new_book)
    await session.flush()

    return new_book


@books_router.get("/", response_model=ReturnedAllBooks)
async def get_all_books(session: DBSession):
    query = select(Book)
    res = await session.execute(query)
    books = res.scalars().all()
    return {"books": books}


@books_router.get("/{book_id}", response_model=ReturnedBook)
async def get_book(book_id: int, session: DBSession):
    return fake_storage[book_id]


@books_router.delete("/{book_id}")
async def delete_book(book_id: int, session: DBSession):

    deleted_book = fake_storage.pop(book_id, -1)
    # print(deleted_book)
    ic(deleted_book)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@books_router.put("/{book_id}")
async def update_book(book_id: int, book: ReturnedBook, session: DBSession):
    if _ := fake_storage.get(book_id, None):
        fake_storage[book_id] = book

    return fake_storage[book_id]
