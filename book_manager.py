import sqlite3
import pandas as pd
import pathlib
import logging

# Configure logging to write to a file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")


# Define the database file in the current root project directory
db_file = pathlib.Path("demoproject.db")

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
    logging.debug("Database created_function completed")

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
    logging.debug("table created_function completed")

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
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)
    
    logging.debug("Ending major_function")
    logging.debug("inserting data_function completed")

def main():
    logging.debug("Starting major_function")

    create_database()
    create_tables()
    insert_data_from_csv()

    logging.debug("Ending major_function")

if __name__ == "__main__":
    main()
