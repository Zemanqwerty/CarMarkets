from pydantic import BaseModel


class CreateFirmaBodyModel(BaseModel):
    name: str


class UpdateFirmaBodyModel(BaseModel):
    name: str


class CreateAutoMarketBodyModel(BaseModel):
    name: str
    firma_id: int


class UpdateAutoMarketBodyModel(BaseModel):
    name: str
    firma_id: int


class CreateCarBodyModel(BaseModel):
    name: str
    number: str
    auto_market_id: int


class UpdateCarBodyModel(BaseModel):
    name: str
    number: str
    auto_market_id: int