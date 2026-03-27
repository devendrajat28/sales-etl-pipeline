# 📊 Sales ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline built with Python and Pandas.

## 🛠️ Tech Stack
- Python 3
- Pandas
- SQLite
- SQL

## 📁 Project Structure
sales_etl_pipeline/
├── data/
│   └── raw_sales.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
└── README.md

## ⚙️ What it Does
- **Extract** — Reads raw sales data from CSV file
- **Transform** — Cleans data:
  - Removes duplicate orders
  - Fills missing customer names
  - Fills missing cities
  - Removes negative quantity orders
  - Calculates total_amount column
- **Load** — Saves clean data into SQLite database

## 🚀 How to Run
# Install dependencies
pip install -r requirements.txt

# Run pipeline
python main.py

## 📊 Sample Output
- Input: 11 raw records
- After cleaning: 9 clean records
- Removed: 1 duplicate + 1 negative quantity

## 👨‍💻 Author
Devendr Jat — B.Tech CSE, JNCT Bhopal
```

---

# Step 2 — requirements.txt Banao

Project folder mein `requirements.txt` file banao:
```
pandas
```

---

# Step 3 — .gitignore Banao

`.gitignore` file banao — yeh important hai!
```
# Database file mat upload karo
data/sales.db

# Python cache
__pycache__/
*.pyc
.env

# VS Code
.vscode/