from pydantic import BaseModel, ConfigDict, Field, HttpUrl
class ListingOut(BaseModel):
    id: int
    source: str
    make: str
    model: str
    year: int
    price_aud: int
    odometer_km: int
    state: str
    suburb: str
    listing_url: str
    model_config = ConfigDict(from_attributes=True)
class ListingCreate(BaseModel):
    source: str = Field(min_length=2, max_length=80)
    source_listing_id: str = Field(min_length=1, max_length=180)
    make: str
    model: str
    year: int = Field(ge=1950, le=2035)
    price_aud: int = Field(gt=0)
    odometer_km: int = Field(ge=0)
    state: str = Field(pattern=r"^(NSW|VIC|QLD|SA|WA|TAS|NT|ACT)$")
    suburb: str = ""
    transmission: str = ""
    body_type: str = ""
    listing_url: HttpUrl
