def transform_dim_geography(df):
    
    dim_geography = df.copy()
    
    dim_geography['STATE'] = (
        dim_geography['STATE']
        .fillna('Unknown')
    )
    
    dim_geography['POSTALCODE'] = (
        dim_geography['POSTALCODE']
        .fillna('Unknown')
    )
    
    dim_geography["TERRITORY"] = (
        dim_geography["TERRITORY"]
        .fillna("Unknown")
    )
    
    dim_geography = (
        dim_geography[
            [
                "ADDRESSLINE1",
                "CITY",
                "STATE",
                "POSTALCODE",
                "COUNTRY",
                "TERRITORY"
            ]
        ]
        .rename(
            columns={
                "ADDRESSLINE1": "address_line1",
                "CITY": "city",
                "STATE": "state",
                "POSTALCODE": "postal_code",
                "COUNTRY": "country",
                "TERRITORY": "territory"
            }
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )
    
    string_columns = [
        "address_line1",
        "city",
        "state",
        "postal_code",
        "country",
        "territory"
    ]

    dim_geography[string_columns] = (
        dim_geography[string_columns]
        .apply(lambda col: col.str.strip())
    )
    
    return dim_geography