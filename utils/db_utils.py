import pyodbc
import pandas as pd

def get_data():
    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-7PL2G9M;"  # ← change this to your actual server name
        "Database=ShoppingDB;"              # ← your database name
        "Trusted_Connection=yes;"
    )

    connection = pyodbc.connect(conn_str)
    df = pd.read_sql("SELECT * FROM shopping_data", connection)
    connection.close()
    return df

