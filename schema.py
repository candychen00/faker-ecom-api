from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, UTC, date

"""
CUSTOMER
"""
class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    state: str
    signup_date: date
    created_at: datetime | None = Field(default_factory=lambda: datetime.now(tz=UTC))


class CustomerCreate(CustomerBase):
    pass


"""
PRODUCTS
"""
class ProductBase(BaseModel):
    product_id: int
    fruit: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

