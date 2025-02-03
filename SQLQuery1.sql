CREATE CERTIFICATE Passwords1
WITH SUBJECT = 'Passwords';
GO

CREATE SYMMETRIC KEY Pass_Key_01
	WITH ALGORITHM = AES_256
	ENCRYPTION BY CERTIFICATE Passwords1;
GO

USE [Practice];
GO

ALTER TABLE dbo.Login
	ADD EncryptedPassword varbinary(128);
GO

OPEN SYMMETRIC KEY Pass_Key_01
	DECRYPTION BY CERTIFICATE Passwords1;

UPDATE dbo.Login
SET EncryptedPassword = ENCRYPTBYKEY(KEY_GUID('Pass_Key_01'), Password);
GO

SELECT Password, EncryptedPassword
	AS 'Encrypted Password',
	CONVERT(nvarchar, DECRYPTBYKEY(EncryptedPassword))
	AS 'Decrypted Password'
	FROM dbo.Login;
GO