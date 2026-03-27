import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "raw_sales.csv")
    db_path   = os.path.join(base_dir, "data", "sales.db")

    print("🚀 ETL Pipeline Starting...")

    # Step 1: Extract
    print("\n📥 Step 1: Extracting data...")
    df = extract_data(file_path)

    # Step 2: Transform
    print("\n⚙️  Step 2: Transforming data...")
    transformed = transform_data(df)

    # Step 3: Load
    print("\n💾 Step 3: Loading data...")
    load_data(transformed, db_path)

    print("\n✅ ETL Pipeline Complete!")