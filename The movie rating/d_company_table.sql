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
INSERT INTO d_company(id, company_name)
 VALUES 
 (11, '20th Century Fox'),
 (12, 'Metro-Goldwyn-Mayer'),
 (13, 'Sony Pictures Classics'),
 (14, 'DreamWorks Pictures'),
 (15, 'Focus Features'),
 (16, 'Lionsgate Films'),
 (17, 'A24 Films'),
 (18, 'Searchlight Pictures'),
 (19, 'Magnolia Pictures'),
 (20, 'IFC Films');



SELECT  * FROM d_company;



