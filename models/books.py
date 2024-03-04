from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

autor_and_title_length = {str: String(length=50)}


class Book(BaseModel):
    __tablename__ = "books_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int]
    count_pages: Mapped[int]
