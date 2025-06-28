-- Rename the column first (uncomment the appropriate line for your DBMS):

-- For SQL Server:
EXEC sp_rename 'movies.rating', 'ratings', 'COLUMN';

-- For PostgreSQL or MySQL 8+:
--ALTER TABLE movies RENAME COLUMN imdb_rating TO rating;

-- Now run your queries after the column has been renamed:
SELECT * FROM movies;
SELECT * FROM movies WHERE ratings > 8.0;

SELECT  * FROM movies  
WHERE rating > 8.0
ORDER BY rating DESC;

SELECT d_company.company_name, COUNT(*) AS movie_count
FROM movies
JOIN d_company ON movies.id = d_company.id
GROUP BY d_company.company_name;

UPDATE movies 
SET movie_title = 'The Professional (Léon)' 
WHERE id = 25;
 