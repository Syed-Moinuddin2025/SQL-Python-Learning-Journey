 TRUNCATE TABLE d_company;
 TRUNCATE TABLE movies;    

 ALTER TABLE movies
DROP CONSTRAINT FK_d_company_id;

USE MovieRating;
GO

BULK INSERT d_company
FROM 'D:\SQL-Python_Journey\The movie rating\d_company_table.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
);

SELECT *
FROM d_company;     

IF OBJECT_ID('movies', 'U') IS NOT NULL
    DROP TABLE movies;
GO

-- ✅ Step 2: Create table
CREATE TABLE movies (
    id INT PRIMARY KEY,
    movie_title VARCHAR(200),
    imdb_rating DECIMAL(3,1),
    year_released INT,
    budget DECIMAL(10,2),
    box_office DECIMAL(10,2),
    d_company_id INT,
    language VARCHAR(100)
);

IF OBJECT_ID('movies', 'U') IS NOT NULL
    DROP TABLE movies;
GO

CREATE TABLE movies (
    id INT PRIMARY KEY,
    movie_title VARCHAR(200),
    imdb_rating DECIMAL(3,1),
    year_released INT,
    budget DECIMAL(10,2),
    box_office DECIMAL(10,2),
    d_company_id INT,
    language VARCHAR(100)
);
SELECT *
FROM movies;

BULK INSERT movies
FROM 'D:\SQL-Python_Journey\The movie rating\movies_tabe.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);