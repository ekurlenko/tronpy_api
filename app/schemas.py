from decimal import Decimal

from pydantic import BaseModel


class Address(BaseModel):
    address: str


class AccountData(BaseModel):
    balance: Decimal
    energy: int
    bandwidth: int


class ExceptionMessage(BaseModel):
    detail: str


class WalletsResponse(BaseModel):
    id: int
    address: str

    class Config:
        from_attributes = True
