-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;


-- Create the books table
-- Note that the books table has no foreign keys, so it is a standalone table
-- All other tables will be connected to books in someway due to it being a standalone table

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
);

-- Create the authors table 
-- Note that the authors table has a foreign key to the books table
-- This means that the authors table is dependent on the books table

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    year_born INTEGER,
    FOREIGN KEY (author_id) REFERENCES books(author_id)
);

-- Create the library table
-- Note that the library table has a foreign key to the book id table
-- The library table is dependent on the books table

CREATE TABLE library (
    location_id INTEGER PRIMARY KEY,
    library_name TEXT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
    street_address TEXT
);

