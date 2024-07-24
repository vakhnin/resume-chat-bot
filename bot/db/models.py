from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Image(Base):
    __tablename__ = 'image'
    __table_args__ = (UniqueConstraint('catalog', 'file_name'),)
    image_id: Mapped[int] = mapped_column(primary_key=True)
    catalog: Mapped[Optional[str]]
    file_name: Mapped[str]
    caption: Mapped[Optional[str]]
    server_image_id: Mapped[str]
    server_image_id_date: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Image(id={self.image_id!r}, catalog={self.catalog!r}, file_name={self.file_name!r})"
