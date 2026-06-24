def transform_dim_product(df):
    dim_product = (
        df[
            [
                "PRODUCTCODE",
                "PRODUCTLINE",
                "MSRP"
            ]
        ]
        .rename(columns={
            "PRODUCTCODE": "product_code",
            "PRODUCTLINE": "product_line",
            "MSRP": "msrp"
        })
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_product