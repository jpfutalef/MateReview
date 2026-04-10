import pandas as pd


def read_csv(filename):
    # Read the csv
    df = pd.read_csv(filename)

    return column_cleaning(df)
    

def column_cleaning(df):
    # Create a mapping for columns names that default to standardized names
    map = {
        "subtypeDescription": "Document Type",
        "title": "Title",
        "description": "Abstract",
        "doi": "DOI"
    }

    df = df.rename(columns=map)

    # Extract year from column 'coverDate' that is a datetime (YYYY-MM-DD)
    if 'Year' not in df.columns and 'coverDate' in df.columns:
        df['Year'] = pd.to_datetime(df['coverDate'], errors='coerce').dt.year

    return df