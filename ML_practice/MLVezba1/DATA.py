import dodaj as d
import pandas as pd
import os

def load_housing_data(housing_path=d.HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)