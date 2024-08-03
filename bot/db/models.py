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
    image_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    catalog: Mapped[Optional[str]]
    file_name: Mapped[str]
    caption: Mapped[Optional[str]]
    server_image_id: Mapped[str]
    server_image_id_date: Mapped[str] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"Image(id={self.image_id!r}, catalog={self.catalog!r}, file_name={self.file_name!r})"


class ProjectsListProjectstAssociation(Base):
    __tablename__ = "projects_list_project_association_table"
    project_id: Mapped[int] = mapped_column(ForeignKey("project.project_id"), primary_key=True)
    projects_list_id: Mapped[int] = mapped_column(
        ForeignKey("project_list.projects_list_id"), primary_key=True
    )
    order: Mapped[int]
    projects: Mapped["Project"] = relationship(back_populates="projects_list")
    projects_list: Mapped["ProjectsList"] = relationship(back_populates="projects")


class Project(Base):
    __tablename__ = 'project'
    project_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    button_title: Mapped[str]
    description_for_skills: Mapped[str]
    shot_description: Mapped[str]
    description: Mapped[str]
    projects_list: Mapped[list['ProjectsList']] \
        = relationship("ProjectsListProjectstAssociation", back_populates="projects")


class ProjectsList(Base):
    __tablename__ = 'project_list'
    projects_list_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    projects: Mapped[list['Project']] \
        = relationship("ProjectsListProjectstAssociation", back_populates="projects_list")
