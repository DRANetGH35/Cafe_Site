from flask_login import UserMixin
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from extensions import db

class cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    map_url: Mapped[str] = mapped_column(String(1000))
    img_url: Mapped[str] = mapped_column(String(1000))
    location: Mapped[str] = mapped_column(String(1000))
    has_sockets: Mapped[bool] = mapped_column(Boolean)
    has_toilet: Mapped[bool] = mapped_column(Boolean)
    has_wifi: Mapped[bool] = mapped_column(Boolean)
    can_take_calls: Mapped[bool] = mapped_column(Boolean)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False)
    seats: Mapped[str] = mapped_column(String(1000))
    coffee_price: Mapped[str] = mapped_column(String(1000))
