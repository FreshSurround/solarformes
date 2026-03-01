from pydantic import BaseModel
from typing import Optional


class Country(BaseModel):
    name: str
    code: str


class Indicator(BaseModel):
    name: str
    code: str
    category: str  # ej: "CO2", "methane", "energy", etc.


class EmissionRecord(BaseModel):
    country_code: str
    indicator_code: str
    year: int
    value: Optional[float]  # puede venir vacío en algunos años


class User(BaseModel):
    id: int
    email: str
    hashed_password: str


class UserInterest(BaseModel):
    user_id: int
    country_code: str
    indicator_code: str
