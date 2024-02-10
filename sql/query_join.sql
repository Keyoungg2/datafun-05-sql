-- Query to inner join library and books table to display library location and book information
SELECT libraries.location_id, libraries.library, books.book_id, books.title,books.year_published
FROM libraries
INNER JOIN books on libraries.book_id = books.book_id;