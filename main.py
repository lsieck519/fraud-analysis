import sqlite3
import pandas as pd
import os
import logging
import numpy as np

# Set up logging for tracking the script's progress and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file paths relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  
RAW_DATA_PATH = os.path.join(SCRIPT_DIR, "./raw-data")  
QUERY_PATH = os.path.join(SCRIPT_DIR, "./sql-queries")  
QUERY_RESULTS_PATH = os.path.join(SCRIPT_DIR, "query_results")
DB_NAME = os.path.join(SCRIPT_DIR, "fraud_data.db") 

# Paths to raw CSV files
CSV_FILES = {
    "fraud1": os.path.join(RAW_DATA_PATH, "fraud-data-1.csv"),
    "fraud2": os.path.join(RAW_DATA_PATH, "fraud-data-2.csv"),
}

def create_database():
    """Create a fresh SQLite database, deleting the old one if it exists."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        logging.info(f"Existing database '{DB_NAME}' deleted.")
    
    with sqlite3.connect(DB_NAME):
        logging.info(f"Database '{DB_NAME}' created successfully.")

def load_csv_to_db():
    """Load all raw CSV files into the SQLite database as tables."""
    with sqlite3.connect(DB_NAME) as conn:
        for table_name, file_path in CSV_FILES.items():
            if os.path.exists(file_path):
                try:
                    # Load all values as strings and replace NaN with empty string
                    df = pd.read_csv(file_path, dtype=str).fillna("")
                    
                    if df.empty:
                        logging.warning(f"Skipping empty cleaned data for table '{table_name}'.")
                        continue

                    # Load into SQLite
                    df.to_sql(table_name, conn, if_exists="replace", index=False)
                    logging.info(f"Loaded '{file_path}' into '{table_name}' table with {len(df)} rows.")
                except Exception as e:
                    logging.error(f"Error loading CSV '{file_path}' into table '{table_name}': {e}")
            else:
                logging.warning(f"File '{file_path}' not found. Skipping...")

def read_sql_file(file_name):
    """Read a SQL file and return its contents as a string."""
    query_file_path = os.path.join(QUERY_PATH, file_name)
    try:
        if os.path.exists(query_file_path):
            with open(query_file_path, 'r') as file:
                return file.read()
        else:
            logging.warning(f"SQL file '{file_name}' not found.")
            return None
    except Exception as e:
        logging.error(f"Error reading SQL file '{file_name}': {e}")
        return None

def run_query(query):
    """Execute a SQL query against the database and return the results as a DataFrame."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            result = pd.read_sql_query(query, conn)
            logging.info(f"Query returned {len(result)} rows.")
            return result
    except Exception as e:
        logging.error(f"Error running SQL query: {e}")
        return pd.DataFrame()

def save_query_results(df, query_name):
    """Save the query result DataFrame to a CSV file in the query_results folder."""
    if not os.path.exists(QUERY_RESULTS_PATH):
        os.makedirs(QUERY_RESULTS_PATH)
    
    result_file_path = os.path.join(QUERY_RESULTS_PATH, f"{query_name}.csv")
    df.to_csv(result_file_path, index=False)
    logging.info(f"Query results saved to '{result_file_path}'")

def main():
    """Main workflow to create database, load data, run queries, and save results."""
    create_database()
    load_csv_to_db()

    query_files = [
        "gap-analysis.sql",
        "fraud-trends.sql",
        "phone-numbers.sql"
    ]

    for query_file in query_files:
        logging.info(f"\nRunning query from file: {query_file}")
        sql = read_sql_file(query_file)
        if sql:
            result_df = run_query(sql)
            if not result_df.empty:
                save_query_results(result_df, query_file.split('.')[0])
            else:
                logging.warning(f"No results returned for query '{query_file}'.")

if __name__ == "__main__":
    main()
