USE [project]
GO
/****** Object:  UserDefinedFunction [dbo].[countperson]    Script Date: 12/27/2023 12:25:44 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER function [dbo].[countperson]()
returns int
as
begin
declare @count int 
select @count=count(*)
from persons
return @count
end

create function [dbo].[two_countperson]()
returns table 
as 

return select * from persons;

print [dbo].[two_countperson]()