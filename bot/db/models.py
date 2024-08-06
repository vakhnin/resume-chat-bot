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
    file_name: Mapped[str]  # необходимо переименовать в source_file
    caption: Mapped[Optional[str]]
    server_image_id: Mapped[str]
    server_image_id_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Image(id={self.id!r}, catalog={self.catalog!r}, file_name={self.file_name!r})"


class Page(Base):
    __tablename__ = "page"
    __mapper_args__ = {'polymorphic_identity': 'page'}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    catalog: Mapped[str]
    source_file: Mapped[str]
    name: Mapped[str]
    content: Mapped[str]


class Project(Page):
    __tablename__ = "project"
    __mapper_args__ = {'polymorphic_identity': 'project'}
    id: Mapped[int] = mapped_column(ForeignKey("page.id"), primary_key=True)
    button_title: Mapped[str]
    for_skills_content: Mapped[str]
    shot_content: Mapped[str]
    projects_list: Mapped[list["ProjectsList"]] \
        = relationship("ProjectListAssociation", back_populates="project")


class ProjectsList(Base):
    __tablename__ = "project_list"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    projects: Mapped[list['Project']] = relationship("ProjectListAssociation", back_populates="projects_list",
                                                     order_by="ProjectListAssociation.order")


class ProjectListAssociation(Base):
    __tablename__ = "projects_list_association"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), primary_key=True)
    projects_list_id: Mapped[int] = mapped_column(ForeignKey("project_list.id"), primary_key=True)
    order: Mapped[int]
    project: Mapped["Project"] = relationship("Project", back_populates="projects_list")
    projects_list: Mapped["ProjectsList"] = relationship("ProjectsList", back_populates="projects")
