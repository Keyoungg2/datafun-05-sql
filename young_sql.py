"""
   This project is to demonstrate the usage of SQL and Python together. We will use Python and SQLite together to excute sql queries that will involve creating and mangaging databases.
   We will be using different CRUD operations ( Select, Update, etc), joins, and other aggreations to for analysis and creation purposes. 
   
  Code Writer: Kareem Young
  creation date: 02/05/2024
"""

#Imported Standard Libraries 
import sqlite3
import pyarrow 
import csv
import pathlib
import logging
import pandas as pd

#Imported External libraries
import uuid

# Logging Configuration - Configure logging to write to a file, appending new logs to the existing file

logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

#Database schema 
''' 
Review Read me and tables in repository or Database Scheme. 
3 tables: Books, Authors, and Libraries
Primary key: book_id
Forgein key:
'''
# Define the database file in the current root project directory
db_file = pathlib.Path("library_operation.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    logging.debug("Starting major_function")

    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

    logging.debug("Ending major_function")
    logging.info("Database created_function completed")

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    logging.debug("Starting major_function")

    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql","create_table.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

    logging.debug("Ending major_function")
    logging.info("table created_function completed")

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    logging.debug("Starting major_function")

    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        libraries_data_path = pathlib.Path("data", "libraries.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        libraries_df = pd.read_csv(libraries_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)
    
    logging.debug("Ending major_function")
    logging.info("inserting data_function completed")

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
    logging.debug("Ending major_function")
    logging.info("Executed SQL from {sql_file}")


def main():
    logging.debug("Starting major_function")

    create_database()
    create_tables()
    insert_data_from_csv()
    
    db_filepath = pathlib.Path("C:\Users\keyou\Documents\CSIS 44609\MOD 5 Python and SQL\datafun-05-sql\library_operation.db")
    execute_sql_from_file(db_filepath, 'sql_file/create_tables.sql')
    execute_sql_from_file(db_filepath, 'sql_file/insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql_file/query_join.sql')


    logging.debug("Ending major_function")
    logging.info("All python commands excuted")
if __name__ == "__main__":
    main()