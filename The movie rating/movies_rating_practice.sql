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
 
ALTER TABLE movies
ADD CONSTRAINT fk_movies_d_company
FOREIGN KEY (d_company_id)
REFERENCES d_company(id);

sp_help movies;
sp_help d_company;

ALTER TABLE movies
ALTER COLUMN d_company_id INT;

ALTER TABLE movies
ADD CONSTRAINT fk_movies_d_company
FOREIGN KEY (d_company_id)
REFERENCES d_company(id);



SELECT TOP 10
    m.movie_title,
    d.company_name
FROM movies m
JOIN d_company d ON m.d_company_id = d.id;

SELECT TOP 20
    m.id AS movie_id,
    m.movie_title,
    m.year_released,
    d.company_name,
    m.imdb_rating,
    m.language
FROM movies m
JOIN d_company d ON m.d_company_id = d.id
ORDER BY m.year_released;