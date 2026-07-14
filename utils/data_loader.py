import pandas as pd
import os


DATA_PATH = "data/customers.csv"


def load_customers():

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        return df

    else:
        raise FileNotFoundError(
            "Customer dataset not found. Run generate_data.py first."
        )