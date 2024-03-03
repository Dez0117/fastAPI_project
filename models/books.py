from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

autor_and_title_length = {str: String(length=50)}


class Book(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]  # type: ignore
    author: Mapped[str]  # type: ignore
    year: Mapped[int]
    count_pages: Mapped[int]
