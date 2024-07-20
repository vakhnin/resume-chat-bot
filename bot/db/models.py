from datetime import datetime
from typing import Optional

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Image(Base):
    __tablename__ = 'image'
    image_id: Mapped[int] = mapped_column(primary_key=True)
    catalog: Mapped[Optional[str]]
    file_name: Mapped[str]
    file_date: Mapped[datetime]
    caption: Mapped[Optional[str]]
    server_image_id: Mapped[str]
    server_image_id_date: Mapped[str]

    def __repr__(self) -> str:
        return f"Image(id={self.image_id!r}, catalog={self.catalog!r}, file_name={self.file_name!r})"
