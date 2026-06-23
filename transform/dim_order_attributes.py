def transform_dim_order_attributes(df):
    
    dim_order_attributes = (
        df[
            [
                "STATUS",
                "DEALSIZE"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_order_attributes