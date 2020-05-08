Select * from tblGender
Select * from tblPerson

Insert into tblPerson (ID, Name, Email,GenderId) Values (10, 'Johnny','j@r.com',NULL)

ALTER TABLE tblPerson
DROP CONSTRAiNT DF_tblPerson_GenderId

ALTER TABLE tblPerson
ADD CONSTRAINT DF_tblPerson_GenderId
DEFAULT 3 FOR GENDERID