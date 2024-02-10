-- This query will provide the average year published from the books table
SELECT AVG(year_published) AS average_published_year
FROM books;

-- This query will count the number of libraries in the libraries table
SELECT COUNT(*) AS library_count
FROM libraries;

-- This query will sum the years as total_published_years in the books table
SELECT SUM(year_published) AS total_published_years
FROM books;