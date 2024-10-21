from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class UserEventsOrm(Base):

    __tablename__ = "user_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"))
