import pandas as pd
from src.utils.schema import DataSchema

destinations_df = None


def load_excel(file_path):
    global destinations_df
    destinations_df = pd.read_excel(file_path)
    return f"Excel loaded with {len(destinations_df)} destinations."


def get_destination_info(name):
    global destinations_df
    df = destinations_df[
        destinations_df[DataSchema.DESTINATION].str.lower() == name.strip().lower()
    ]
    return df.iloc[0].to_dict() if len(df) else None
