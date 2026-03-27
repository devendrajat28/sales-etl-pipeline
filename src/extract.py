import pandas as pd
import logging
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(file_path):

    try:
        data = pd.read_csv(file_path)
        logging.info(f"data extracted successfully from {file_path}")
        logging.info(f"Extracted {data.shape[0]} rows and {data.shape[1]} columns")

        return data
    except FileNotFoundError:
        logging.error(f"file not found: {file_path}")
    except Exception as e:
        logging.error(f"an error occurred while extracting data: {e}")

if __name__ == "__main__":
    # Current file ki location se path banao
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "raw_sales.csv")
    
    df = extract_data(file_path)
    if df is not None:
        print(df.head())
        print(df.shape)
    else:
        print("Data loading failed ❌")

