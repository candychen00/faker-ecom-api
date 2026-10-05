from faker import Faker
from datetime import date

from fastapi import Query, APIRouter, Depends
from main import verify_api_key

Faker.seed(1234)
fake = Faker('en_US')

router = APIRouter(
    prefix="/customers", 
    tags=["customers"],
    dependencies=[Depends(verify_api_key)],
)


@router.get("/fake_customers")
def get_fake_customers(
            num: int = Query(default=1, ge=1, le=20),
            api_key: str = Depends(verify_api_key)
    ):
    cust_to_return = []
    for i in range(num):
        cust_to_return.append(
            {
                "customer_id": fake.uuid4(),
                'name': fake.name(),
                'email': fake.email(),
                'state': fake.state(),
                'signup_date': fake.date_between(start_date= date(2026, 1, 1), end_date=date(2026, 6, 30)),
            }
        )
    return cust_to_return



