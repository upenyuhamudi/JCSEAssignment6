CREATE DATABASE college;
CREATE TABLE student(
	studentid integer NOT NULL PRIMARY KEY,
   Firstname   VARCHAR(6) NOT NULL 
  ,Surname     VARCHAR(8) NOT NULL
  ,Algebra     INTEGER  NOT NULL
  ,Calculus    INTEGER  NOT NULL
  ,Programming INTEGER  NOT NULL
  ,DBases   INTEGER  NOT NULL
);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('1','Joe','Soap',92,78,65,67);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('2','Jane','Doe',81,79,83,89);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('3','Mary','Poppins',63,52,65,71);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('4','Mario','Rossi',23,42,50,44);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('5','John','Smith',56,67,72,72);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('6','Tom','Cruz',81,62,53,59);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('7','Jim','Beglin',41,48,51,53);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('8','Peter','Shmooks',55,55,66,58);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('9','Hans','Meier',57,87,95,64);
INSERT INTO student(studentid,Firstname,Surname,Algebra,Calculus,Programming,DBases) VALUES ('10','Jackie','Brown',97,91,86,73);

CREATE TABLE grades(
	studentid integer NOT NULL PRIMARY KEY,
   Firstname   VARCHAR(6) NOT NULL 
  ,Surname     VARCHAR(8) NOT NULL
  ,Average     INTEGER  NOT NULL
  ,Grade     VARCHAR(8) NOT NULL
);
