CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
	)
	INSERT INTO Users (name, email) VALUES ('kRISTIN', 'KF@IMICH.EDU')
	DELETE FROM Users WHERE email = 'KF@IMICH.EDU'
	UPDATE Users SET name = 'Mehmet Yilmaz' WHERE email= 'vlt@umicedu.com'

	SELECT * FROM Users
	SELECT * FROM Users WHERE email = 'vlt@umicedu.com'
	SELECT * from Users ORDER BY name
	SELECT * FROM Users ORDER BY email