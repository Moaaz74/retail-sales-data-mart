from load.load_dimensions import load_dimension

def load_all_dimensions(dimensions):
    
    load_dimension(dimensions['dim_date'], 'dim_date')
    load_dimension(dimensions['dim_product'], 'dim_product')
    load_dimension(dimensions['dim_customer'], 'dim_customer')
    load_dimension(dimensions['dim_geography'], 'dim_geography')
    load_dimension(dimensions['dim_order_attributes'], 'dim_order_attributes')
    print("\n✔ All dimensions loaded successfully into the database.")