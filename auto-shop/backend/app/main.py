from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from .db import Base, engine, get_db
from .models import VehicleListing
from .schemas import ListingOut, ListingCreate
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Auto Shop API", version="0.1.0", description="Australian vehicle discovery API")
@app.get("/health")
def health(): return {"status":"ok","market":"AU"}
@app.get("/api/listings", response_model=list[ListingOut])
def list_listings(make: str|None=None, state: str|None=None, max_price: int|None=Query(default=None,gt=0), db: Session=Depends(get_db)):
    stmt=select(VehicleListing)
    if make: stmt=stmt.where(VehicleListing.make.ilike(f"%{make}%"))
    if state: stmt=stmt.where(VehicleListing.state==state.upper())
    if max_price: stmt=stmt.where(VehicleListing.price_aud<=max_price)
    return list(db.scalars(stmt.order_by(VehicleListing.created_at.desc()).limit(100)).all())
@app.post("/api/listings", response_model=ListingOut, status_code=201)
def create_listing(payload: ListingCreate, db: Session=Depends(get_db)):
    exists=db.scalar(select(VehicleListing).where(VehicleListing.source==payload.source, VehicleListing.source_listing_id==payload.source_listing_id))
    if exists: raise HTTPException(409,"This source listing is already ingested")
    item=VehicleListing(**payload.model_dump())
    db.add(item); db.commit(); db.refresh(item)
    return item
@app.get("/api/valuation-estimate")
def valuation_estimate(make: str, model: str, year: int, odometer_km: int):
    # Intentionally not a real valuation. Replace with a validated model trained on licensed AU data.
    return {"status":"not_configured","currency":"AUD","make":make,"model":model,"year":year,"odometer_km":odometer_km,
            "message":"A production valuation requires licensed Australian market data and a validated model."}
