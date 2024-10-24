from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class EventsOrm(Base):

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[int] = mapped_column(String)
    poster_url: Mapped[str] = mapped_column(String)
    date: Mapped[datetime] = mapped_column(DateTime)
    post_date: Mapped[datetime] = mapped_column(DateTime)
    category: Mapped[str] = mapped_column(String)
    price_from: Mapped[int] = mapped_column(Integer)
    price_to: Mapped[int] = mapped_column(Integer)
    creater_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    likes: Mapped[int] = mapped_column(Integer)
    dislikes: Mapped[int] = mapped_column(Integer)
    views: Mapped[int] = mapped_column(Integer)
