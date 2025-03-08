-- Creating the working Schema
CREATE SCHEMA assignment2_movies;

-- Had to drop and recreate a few times 
-- DROP TABLE assignment2_movies.movies;

-- Creating the empty table to fill in. 
-- Create the table with critics and their ratings for different movies
CREATE TABLE assignment2_movies.critics_ratings (
    critic VARCHAR(50),
    Goodfellas DECIMAL(2, 1),
    VforVendetta DECIMAL(2, 1),
    Arrival DECIMAL(2, 1),
    Inception DECIMAL(2, 1),
    TheWitch DECIMAL(2, 1),
    TheDarkKnight DECIMAL(2, 1)
);

-- Insert the ratings into the table
INSERT INTO assignment2_movies.critics_ratings (critic, Goodfellas, VforVendetta, Arrival, Inception, TheWitch, TheDarkKnight)
VALUES
-- Tom's ratings
('Tom', 4.5, 3.8, NULL, 4.2, 4.0, NULL),

-- John's ratings
('John', 4.0, NULL, 5.0, 3.5, NULL, 4.9),

-- Cat's ratings
('Cat', NULL, 4.1, 5.0, 2.9, 3.7, NULL),

-- Lisa's ratings
('Lisa', 4.5, 4.0, NULL, 3.0, NULL, 4.7),

-- Chris's ratings
('Chris', NULL, 4.2, 4.8, 2.7, 3.0, NULL),

-- Jen's ratings
('Jen', 4.4, 3.9, 4.6, NULL, 4.0, 4.5);

-- Testing what table looks like
Select * from assignment2_movies.critics_ratings limit 10;
