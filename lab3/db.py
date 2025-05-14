from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column, Mapped
from sqlalchemy import Integer, String, Boolean, create_engine


class Base(DeclarativeBase):
    pass


class TODO(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer)
    title: Mapped[String] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean)
