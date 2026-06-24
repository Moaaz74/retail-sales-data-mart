from sqlalchemy import text
from database.connection import engine

def load_dimension(df , table_name):
    
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(text(f"TRUNCATE TABLE dw.{table_name} RESTART IDENTITY CASCADE"))
    
    df.to_sql(
        name=table_name,
        con=engine,
        schema="dw",
        if_exists="append",
        index=False,
    )
    
    print(f"\n✔ {table_name} loaded successfully into the database.")
