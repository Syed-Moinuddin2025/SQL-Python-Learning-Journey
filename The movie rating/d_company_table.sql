--CREATE DATABASE MovieRating;


USE MovieRating;

IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'd_company'
)
BEGIN
    CREATE TABLE d_company (
        id INT PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL
    );
END

 INSERT INTO d_company(id,company_name)
 VALUES
 
 (1, 'Columbia Pictures'),
 (2,  'Paramoun Pictures'),
 (3, 'Warner Bros. Pictures'),
 (4, 'United Artists'),
 (5, 'Universal Pictures'),
 (6,'New Line Cinma'),
 (7,'Miramax Film'),
 (8, 'Produzioni Erepee Associate'),
 (9, 'Buena Vista'),
 (10, 'StudioCanal');



SELECT TOP 5 * FROM d_company;



