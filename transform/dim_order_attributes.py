def transform_dim_order_attributes(df):
    
    dim_order_attributes = (
        df[
            [
                "STATUS",
                "DEALSIZE"
            ]
        ]
        .rename(
            columns={
                "STATUS": "status_name",
                "DEALSIZE": "deal_size"
            }
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return dim_order_attributes