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
        .rename(
            columns={
                "CUSTOMERNAME": "customer_name",
                "CONTACTFIRSTNAME": "contact_first_name",
                "CONTACTLASTNAME": "contact_last_name"
            }
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_customer