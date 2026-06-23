from extract.extract import extract
from transform.dim_product import transform_dim_product
from transform.dim_customer import transform_dim_customer
from transform.dim_geography import transform_dim_geography
from transform.dim_date import transform_dim_date
from transform.dim_order_attributes import transform_dim_order_attributes


def run_all_transformations():

    df = extract()

    print("\n✔ Data Extracted")
    print("Shape:", df.shape)


    dim_product = transform_dim_product(df)
    dim_customer = transform_dim_customer(df)
    dim_geography = transform_dim_geography(df)
    dim_date = transform_dim_date(df)
    dim_order_attributes = transform_dim_order_attributes(df)


    print("\n===== DIMENSIONS SUMMARY =====")

    print("\nDimProduct:", dim_product.shape)
    print("Nulls:\n", dim_product.isnull().sum())

    print("\nDimCustomer:", dim_customer.shape)
    print("Nulls:\n", dim_customer.isnull().sum())

    print("\nDimGeography:", dim_geography.shape)
    print("Nulls:\n", dim_geography.isnull().sum())

    print("\nDimDate:", dim_date.shape)
    print("Nulls:\n", dim_date.isnull().sum())

    print("\nDimOrderAttributes:", dim_order_attributes.shape)
    print("Nulls:\n", dim_order_attributes.isnull().sum())


    return {
        "dim_product": dim_product,
        "dim_customer": dim_customer,
        "dim_geography": dim_geography,
        "dim_date": dim_date,
        "dim_order_attributes": dim_order_attributes
    }
    
