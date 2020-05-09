Select * from tblPerson

Delete from tblPerson where ID = 5
Insert into tblPerson values(5, 'Sarah', 'a@a.com',2, 950)

Alter Table tblPerson
Drop Constraint CK_tblPerson_Age

Alter Table tblPerson
Add Constraint CK_tblePerson_Age CHECK (AGE >0 AND AGE <150)