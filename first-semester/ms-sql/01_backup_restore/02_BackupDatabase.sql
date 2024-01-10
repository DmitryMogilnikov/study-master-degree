USE [master]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Dmitry Mogilnikov
-- Create date: 2022-11-22
-- Description:	Backup Database
-- Variables:
-- databaseName
-- backupType: F=full, D=differential
-- backupLocation: path to backup file
-- =============================================
CREATE PROCEDURE BackupDatabase 
	@databaseName sysname, 
	@backupType CHAR(1) = 'F', --FULL, DIFFIRENTIAL
	@backupLocation nvarchar(200) = "C:\temp\backup\"

AS
BEGIN 
	SET NOCOUNT ON;
	
	DECLARE @fileName VARCHAR(256) -- filename for backup
	DECLARE @fileDate VARCHAR(20) -- used for file name

	SELECT @fileDate = REPLACE(CONVERT(VARCHAR, GETDATE(),111),'/','') + '_' + REPLACE(CONVERT(VARCHAR, GETDATE(),8),':','')
	
	IF @backupType = 'F' 
	BEGIN
            SET @fileName = @backupLocation+REPLACE(REPLACE(@databaseName, '[',''),']','')+ '_FULL_'+ @fileDate+ '.bak' 
			BACKUP DATABASE @databaseName
			TO DISK = @fileName
			WITH INIT
			INSERT INTO Backups 
			VALUES (@fileName, @backupType);
	END

	ELSE IF @backupType = 'D' 
	BEGIN
            SET @fileName = @backupLocation+REPLACE(REPLACE(@databaseName, '[',''),']','')+ '_DIFF_'+ @fileDate+ '.bak' 
			BACKUP DATABASE @databaseName
			TO DISK = @fileName
			WITH DIFFERENTIAL, INIT;
			INSERT INTO Backups 
			VALUES (@fileName, @backupType);
	END

END
GO

--USE [master]
--GO
--EXAMPLE: EXEC BackupDatabase <DatabaseName>, <BackupType> = 'F', 'D', 'L'
