USE [master]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Dmitry Mogilnikov
-- Create date: 2022-11-22
-- Description:	Restore Database
-- Variables:
-- databaseName
-- datetimeToRestore
-- backupLocation: path to backup file
-- =============================================
CREATE PROCEDURE RestoreDatabase 
	@databaseName sysname, 
	@datetimeToRestore datetime,
	@backupLocation nvarchar(200) = "C:\temp\backup\"

AS
BEGIN 
	SET NOCOUNT ON;
	DECLARE @fullBackup VARCHAR(256)
	DECLARE @diffBackup VARCHAR(256)
	DECLARE @fileDate VARCHAR(20)

	SELECT @datetimeToRestore = CONVERT(VARCHAR, CAST(@datetimeToRestore AS DATETIME))

	SELECT @fileDate = REPLACE(CONVERT(VARCHAR, @datetimeToRestore,111),'/','') + '_' + REPLACE(CONVERT(VARCHAR, @datetimeToRestore,8),':','')
	PRINT(@fileDate)

	SELECT @fullBackup = @backupLocation+@databaseName+'_FULL_' + @fileDate + '.bak'
	SELECT @diffBackup = @backupLocation+@databaseName+'_DIFF_' + @fileDate + '.bak'  
	
	SET @fullBackup = (SELECT MAX(filenameBackup)
					  FROM Backups
					  WHERE (filenameBackup <= @fullBackup) AND (typeBackup = 'F'))
	
	SET @diffBackup = (SELECT MAX(filenameBackup)
					  FROM Backups
					  WHERE (filenameBackup <= @diffBackup) AND (typeBackup = 'D'))
	
	RESTORE DATABASE @databaseName FROM DISK = @fullBackup
	WITH NORECOVERY

	RESTORE DATABASE @databaseName FROM DISK = @diffBackup  
	WITH RECOVERY  
	
END
GO

--USE [master]
--GO
--EXAMPLE: EXEC RestoreDatabase <DatabaseName>, <datetimeRestore> IN FORMAT '2022-12-13T16:00:00'




