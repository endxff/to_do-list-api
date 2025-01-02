# Define the database schema.
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# declarative base class
class Base(DeclarativeBase):
    pass


# Create Task Model
class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    done: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"<Task {self.title}>"
