from extract.extract import extract

def transform_dim_customer(df):
    dim_customer = (
        df[
            [
                "CUSTOMERNAME",
                "CONTACTFIRSTNAME",
                "CONTACTLASTNAME"
                
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_customer