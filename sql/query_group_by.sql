-- Query to group books by location id after inner join
SELECT libraries.location_id, libraries.library_name, books.book_id, books.title,books.year_published
FROM libraries
INNER JOIN books on libraries.book_id = books.book_id;