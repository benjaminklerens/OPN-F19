CREATE DATABASE opnexam2019;

USE opnexam2019;

CREATE TABLE persons (
	PersonID int NOT NULL AUTO_INCREMENT,
	Firstname TEXT NOT NULL,
	Lastname TEXT NOT NULL,
	PRIMARY KEY (PersonID)
);
