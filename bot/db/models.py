from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, UniqueConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Image(Base):
    __tablename__ = 'image'
    __table_args__ = (UniqueConstraint('catalog', 'file_name'),)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    catalog: Mapped[Optional[str]]
    file_name: Mapped[str]
    caption: Mapped[Optional[str]]
    server_image_id: Mapped[str]
    server_image_id_date: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Image(id={self.id!r}, catalog={self.catalog!r}, file_name={self.file_name!r})"


class ProjectListAssociation(Base):
    __tablename__ = "projects_list_association"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), primary_key=True)
    projects_list_id: Mapped[int] = mapped_column(ForeignKey("project_list.id"), primary_key=True)
    order: Mapped[int]
    project: Mapped["Project"] = relationship(back_populates="projects_list")
    projects_list: Mapped["ProjectsList"] = relationship(back_populates="projects")


class Project(Base):
    __tablename__ = "project"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    button_title: Mapped[str]
    description_for_skills: Mapped[str]
    shot_description: Mapped[str]
    description: Mapped[str]
    projects_list: Mapped[list["ProjectsList"]] \
        = relationship("ProjectListAssociation", back_populates="project")


class ProjectsList(Base):
    __tablename__ = "project_list"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    projects: Mapped[list['Project']] \
        = relationship("ProjectListAssociation", back_populates="projects_list",
                       order_by="ProjectListAssociation.order")
