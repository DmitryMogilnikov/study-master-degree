SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Dmitry Mogilnikov
-- Create date: 2022-12-01
-- Description:	Check permission for user in system
-- =============================================
CREATE PROCEDURE CheckMyPermission 
AS
BEGIN
	SET NOCOUNT ON;

    SELECT o.name, p.permission_name
	FROM sys.tables o
	CROSS APPLY sys.fn_my_permissions(o.name, 'OBJECT') p
	WHERE p.subentity_name = ''
END
GO

--EXAMPLE:
--USE <name database> 
--GO
--CheckMyPermission 