import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def transform_data(data):
    try:
        initial_rows = len(data)
        logging.info(f"Transform started | Initial rows: {initial_rows}")

        data = data.drop_duplicates(subset=['order_id']).copy()
        logging.info(f"After dedup: {len(data)} rows")

        data['date'] = pd.to_datetime(data['date'], errors='coerce')

        data['customer_name'] = data['customer_name'].fillna('Unknown')
        data['city'] = data['city'].fillna('Unknown')

        data = data[data['quantity'] > 0]

        data['total_amount'] = (
            data['price'] * data['quantity'] * (1 - data['discount'] / 100)
        )

        final_rows = len(data)
        logging.info(f"Transform done | Final rows: {final_rows} | Removed: {initial_rows - final_rows}")

        return data

    except Exception as e:
        logging.error(f"Transform error: {e}")
        return None


if __name__ == "__main__":
    import os, sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from extract import extract_data

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "raw_sales.csv")

    df = extract_data(file_path)
    if df is not None:
        transformed = transform_data(df)
        if transformed is not None:
            print("\nTransformed Data:")
            print(transformed)
            print(f"\nShape: {transformed.shape}")
            print(f"\nNew column total_amount:")
            print(transformed[['order_id', 'price', 'quantity', 'discount', 'total_amount']])