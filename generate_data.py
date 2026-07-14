import pandas as pd
import numpy as np
from faker import Faker
import random
import os

fake = Faker()

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 1000


card_types = [
    "Blue Card",
    "Gold Card",
    "Platinum Card",
    "Travel Card",
    "Premium Card"
]

cities = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata"
]

occupations = [
    "Engineer",
    "Doctor",
    "Business Owner",
    "Consultant",
    "Student",
    "Manager"
]


customers = []

for i in range(1, NUM_CUSTOMERS + 1):

    income = random.randint(300000, 5000000)

    credit_limit = random.randint(
        50000,
        min(income, 1000000)
    )

    monthly_spend = random.randint(
        5000,
        int(credit_limit * 0.8)
    )

    balance = random.randint(
        0,
        monthly_spend
    )

    utilization = round(
        (balance / credit_limit) * 100,
        2
    )

    customers.append({

        "customer_id": f"CUST{i:04}",

        "name": fake.name(),

        "age": random.randint(21,65),

        "city": random.choice(cities),

        "occupation": random.choice(occupations),

        "annual_income": income,

        "card_type": random.choice(card_types),

        "credit_limit": credit_limit,

        "current_balance": balance,

        "monthly_spend": monthly_spend,

        "travel_spend": random.randint(0,200000),

        "dining_spend": random.randint(0,100000),

        "shopping_spend": random.randint(0,150000),

        "reward_points": random.randint(1000,50000),

        "credit_utilization": utilization,

        "late_payments": random.randint(0,5),

        "relationship_years": random.randint(1,15),

        "inactive_days": random.randint(0,180),

        "salary_growth": random.randint(0,30)

    })


df = pd.DataFrame(customers)


df.to_csv(
    "data/customers.csv",
    index=False
)


print("Customer dataset generated successfully!")
print(df.head())