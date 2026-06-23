import pandas as pd

def transform_dim_date(df):
    
    df = df.copy()
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

    dim_date = pd.DataFrame()

    dim_date["full_date"] = (
        df["ORDERDATE"]
        .dt.normalize()
        .drop_duplicates()
        .sort_values()
    )
    
    dim_date['date_key'] = (
        dim_date['full_date']
        .dt.strftime('%Y%m%d')
        .astype(int)
    )  
    
    dim_date['day'] = dim_date['full_date'].dt.day
    dim_date['month'] = dim_date['full_date'].dt.month
    dim_date['year'] = dim_date['full_date'].dt.year
    dim_date['quarter'] = dim_date['full_date'].dt.quarter
    dim_date['day_name'] = dim_date['full_date'].dt.day_name()
    dim_date['month_name'] = dim_date['full_date'].dt.month_name()
    dim_date['is_weekend'] = dim_date['full_date'].dt.weekday >= 5
    dim_date["week_of_year"] = dim_date['full_date'].dt.isocalendar().week
    
    dim_date = dim_date[
        [
            "date_key",
            "full_date",
            "year",
            "quarter",
            "month",
            "month_name",
            "day",
            "day_name",
            "week_of_year",
            "is_weekend"
        ]
    ]
    
    return dim_date