from fastapi.responses import ORJSONResponse
from icecream import ic
from fastapi import Response, status, APIRouter
from schemas import IncomingBook, ReturnedAllBooks, ReturnedBook
from configurations.database import get_async_session

COUNTER = 0  # каунтер имитирующий присвоение id в базе данных

books_router = APIRouter(
    tags=["books"],
    prefix="/books"
)

fake_storage = {}


@books_router.post("/", response_model=ReturnedBook)
async def create_book(book: IncomingBook):
    global COUNTER
    # TODO запись в БД
    new_book = {
        "id": COUNTER,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "count_pages": book.count_pages
        }
    fake_storage[COUNTER] = new_book
    COUNTER += 1
    # return new_book
    return ORJSONResponse(new_book, status_code=status.HTTP_201_CREATED)


@books_router.get("/", response_model=ReturnedAllBooks)
async def get_all_books():
    # Хотим видеть:
    # books: [{"id": 1, "title": "smth", ...}, {"id": 2, ...}]
    # но не можем из-за нашего Response_model
    books = [i for i in fake_storage.values()]
    return {"books": books}


@books_router.get("/{book_id}", response_model=ReturnedBook)
async def get_book(book_id: int):
    return fake_storage[book_id]


@books_router.delete("/{book_id}")
async def delete_book(book_id: int):

    deleted_book = fake_storage.pop(book_id, -1)
    # print(deleted_book)
    ic(deleted_book)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@books_router.put("/{book_id}")
async def update_book(book_id: int, book: ReturnedBook):
    if _ := fake_storage.get(book_id, None):
        fake_storage[book_id] = book

    return fake_storage[book_id]
