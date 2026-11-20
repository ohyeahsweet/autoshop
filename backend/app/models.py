from sqlalchemy import String, Integer, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base
class VehicleListing(Base):
    __tablename__ = "vehicle_listings"
    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(80), index=True)
    source_listing_id: Mapped[str] = mapped_column(String(180), index=True)
    make: Mapped[str] = mapped_column(String(80), index=True)
    model: Mapped[str] = mapped_column(String(100), index=True)
    year: Mapped[int] = mapped_column(Integer, index=True)
    price_aud: Mapped[int] = mapped_column(Integer, index=True)
    odometer_km: Mapped[int] = mapped_column(Integer)
    state: Mapped[str] = mapped_column(String(3), index=True)
    suburb: Mapped[str] = mapped_column(String(100), default="")
    transmission: Mapped[str] = mapped_column(String(40), default="")
    body_type: Mapped[str] = mapped_column(String(50), default="")
    listing_url: Mapped[str] = mapped_column(String(1000))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
