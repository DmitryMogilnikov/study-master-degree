SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Dmitry Mogilnikov
-- Create date: 2022-12-01
-- Description:	Check permission for user in system
-- Variables:
-- userName
-- =============================================
CREATE PROCEDURE CheckUserPermission 
	@userName varchar(100)

AS
BEGIN
	SET NOCOUNT ON;

	SELECT schemas.name AS [Schema], 
		   tables.name AS [Object], 
		   database_principals.name AS [User Name],
		   database_permissions.permission_name, 
		   database_permissions.state_desc

	FROM sys.database_permissions join sys.tables 
		 on sys.database_permissions.major_id = sys.tables.object_id 
		 join sys.schemas on sys.tables.schema_id = sys.schemas.schema_id     
		 join sys.database_principals 
		 on sys.database_permissions.grantee_principal_id =
		 sys.database_principals.principal_id
	
	WHERE sys.database_principals.name = @userName
END
GO

--EXAMPLE: 
--USE <name database>
--GO
--CheckUserPermission <user name>