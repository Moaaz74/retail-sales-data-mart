def transform_dim_product(df):
    dim_product = (
        df[
            [
                "PRODUCTCODE",
                "PRODUCTLINE",
                "MSRP"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_product