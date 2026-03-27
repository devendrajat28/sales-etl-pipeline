import sqlite3
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def load_data(data, db_path):
    try:
        conn = sqlite3.connect(db_path)
        data.to_sql('sales', conn, if_exists='replace', index=False)
        logging.info(f"Data loaded successfully into {db_path}")

        conn.close()
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")

if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from extract import extract_data
    from transform import transform_data

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "raw_sales.csv")
    db_path = os.path.join(base_dir, "data", "sales.db")

    df = extract_data(file_path)
    transformed = transform_data(df)
    load_data(transformed, db_path)

    # Verify — database se data wapas padhlo!
    conn = sqlite3.connect(db_path)
    result = pd.read_sql("SELECT * FROM sales", conn)
    print(result)
    conn.close()