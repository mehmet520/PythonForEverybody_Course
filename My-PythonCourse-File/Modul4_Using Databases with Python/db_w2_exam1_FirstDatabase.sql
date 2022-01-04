-- CREATE TABLE Ages ( name VARCHAR (128), age INTEGER);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Deborah', 14);
INSERT INTO Ages (name, age) VALUES ('Kirstin', 13);
INSERT INTO Ages (name, age) VALUES ('Blaine', 28);
INSERT INTO Ages (name, age) VALUES ('Medeeha', 14);
INSERT INTO Ages (name, age) VALUES ('Sukhman', 18);

SELECT hex (name || age) AS X FROM Ages ORDER BY X;